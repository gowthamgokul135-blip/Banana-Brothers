import sys
import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestBananaBrothersPlatform(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_01_health_and_root(self):
        res = self.client.get("/health")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {"status": "ok"})

        res_root = self.client.get("/")
        self.assertEqual(res_root.status_code, 200)
        self.assertEqual(res_root.json()["status"], "healthy")

    def test_02_services_and_packages_catalog(self):
        # Test services endpoint
        res = self.client.get("/api/v1/services")
        self.assertEqual(res.status_code, 200)
        services = res.json()
        self.assertGreaterEqual(len(services), 12)

        # Test filter by category
        res_filtered = self.client.get("/api/v1/services?category=Weddings")
        self.assertEqual(res_filtered.status_code, 200)
        for s in res_filtered.json():
            self.assertEqual(s["category"], "Weddings")

        # Test packages endpoint
        res_pkg = self.client.get("/api/v1/packages")
        self.assertEqual(res_pkg.status_code, 200)
        packages = res_pkg.json()
        self.assertEqual(len(packages), 3)

    def test_03_booking_calculation(self):
        # 1 day test
        calc_payload = {
            "package_tier": "high",
            "needs_values": [40000, 20000],
            "from_date": "2026-11-10",
            "to_date": "2026-11-10"
        }
        res = self.client.post("/api/v1/bookings/calculate", json=calc_payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["duration_days"], 1)
        self.assertEqual(data["base_amount"], 150000.0)
        self.assertEqual(data["total_estimated_amount"], 210000.0)

        # 3 days test
        calc_multi_day = {
            "package_tier": "medium",
            "needs_values": [25000],
            "from_date": "2026-11-10",
            "to_date": "2026-11-12"
        }
        res_multi = self.client.post("/api/v1/bookings/calculate", json=calc_multi_day)
        self.assertEqual(res_multi.status_code, 200)
        data_multi = res_multi.json()
        self.assertEqual(data_multi["duration_days"], 3)
        self.assertEqual(data_multi["total_estimated_amount"], (75000.0 + 25000.0) * 3)

    def test_04_auth_customer_and_admin_flows(self):
        import uuid
        test_username = f"user_{uuid.uuid4().hex[:6]}"
        test_email = f"{test_username}@example.com"

        # Register User
        reg_payload = {
            "firstName": "Gowtham",
            "lastName": "Kumar",
            "username": test_username,
            "email": test_email,
            "age": 23,
            "password": "Password@123",
            "confirmPassword": "Password@123"
        }
        reg_res = self.client.post("/api/v1/auth/register", json=reg_payload)
        self.assertEqual(reg_res.status_code, 200)
        user_data = reg_res.json()
        self.assertIn("access_token", user_data)
        self.assertEqual(user_data["user"]["role"], "USER")
        user_token = user_data["access_token"]

        # User profile
        me_res = self.client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {user_token}"})
        self.assertEqual(me_res.status_code, 200)
        self.assertEqual(me_res.json()["username"], test_username)

        # Customer attempts to access Admin endpoint (must be rejected 403 Forbidden)
        admin_res_forbidden = self.client.get("/api/v1/admin/stats", headers={"Authorization": f"Bearer {user_token}"})
        self.assertEqual(admin_res_forbidden.status_code, 403)

        # Admin Login
        admin_login_payload = {
            "username": "admin",
            "password": "Admin@123"
        }
        admin_login_res = self.client.post("/api/v1/auth/login", json=admin_login_payload)
        self.assertEqual(admin_login_res.status_code, 200)
        admin_token = admin_login_res.json()["access_token"]
        self.assertEqual(admin_login_res.json()["user"]["role"], "ADMIN")

        # Admin accesses stats
        admin_stats_res = self.client.get("/api/v1/admin/stats", headers={"Authorization": f"Bearer {admin_token}"})
        self.assertEqual(admin_stats_res.status_code, 200)
        self.assertIn("total_bookings", admin_stats_res.json())

    def test_05_booking_creation_and_admin_status_update(self):
        # Submit booking
        booking_payload = {
            "package_tier": "high",
            "fullName": "Karthik Subramanian",
            "mobileNo": "9876543210",
            "emailAddr": "karthik@example.com",
            "functionType": "Wedding (Thirumanam)",
            "needs": ["Food", "DJ Music", "Photography"],
            "districtSelect": "Coimbatore",
            "place": "RS Puram",
            "fullAddress": "No. 45, Avinashi Road, RS Puram",
            "pincode": "641002",
            "fromDate": "2026-12-15",
            "toDate": "2026-12-15",
            "fromTime": "09:00",
            "toTime": "22:00",
            "mapLocation": "https://maps.google.com/?q=Coimbatore"
        }
        book_res = self.client.post("/api/v1/bookings", json=booking_payload)
        self.assertEqual(book_res.status_code, 200)
        book_data = book_res.json()
        self.assertTrue(book_data["success"])
        booking_id = book_data["booking_id"]
        booking_ref = book_data["booking_reference"]

        # Admin queries all bookings
        admin_login = self.client.post("/api/v1/auth/login", json={"username": "admin", "password": "Admin@123"}).json()
        admin_token = admin_login["access_token"]

        admin_bookings = self.client.get("/api/v1/admin/bookings", headers={"Authorization": f"Bearer {admin_token}"})
        self.assertEqual(admin_bookings.status_code, 200)
        found = any(b["id"] == booking_id for b in admin_bookings.json())
        self.assertTrue(found)

        # Admin updates status to COMPLETED
        update_res = self.client.patch(
            f"/api/v1/admin/bookings/{booking_id}/status",
            json={"status": "COMPLETED"},
            headers={"Authorization": f"Bearer {admin_token}"}
        )
        self.assertEqual(update_res.status_code, 200)
        self.assertEqual(update_res.json()["status"], "COMPLETED")

if __name__ == "__main__":
    unittest.main()
