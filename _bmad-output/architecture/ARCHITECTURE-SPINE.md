---
name: Banana Brothers Events Platform Architecture
type: architecture-spine
purpose: build-substrate
altitude: feature
paradigm: Client-Server 3-Tier Layered REST Architecture (React SPA + FastAPI + MySQL)
scope: Full-stack web application encompassing UI conversion, REST APIs, and relational persistence
status: final
created: '2026-09-20'
updated: '2026-09-20'
binds:
  - FR-1
  - FR-2
  - FR-3
  - FR-4
  - FR-5
  - FR-6
  - FR-7
  - FR-8
  - FR-9
  - FR-10
  - FR-11
  - UJ-1
  - UJ-2
  - UJ-3
sources:
  - _bmad-output/planning-artifacts/prds/prd-banana-brothers-events-2026-09-20/prd.md
  - _bmad-output/planning-artifacts/ux-designs/ux-banana-brothers-events-2026-09-20/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-banana-brothers-events-2026-09-20/EXPERIENCE.md
companions: []
---

# Architecture Spine — Banana Brothers Events Platform

## 1. Design Paradigm

The system implements a **3-Tier Layered Architecture** with strict separation of concerns between presentation, business orchestration, and relational persistence:

```mermaid
graph TD
    subgraph Presentation Tier [Frontend: React.js SPA (JS/JSX)]
        UI[Views & Components - 1:1 HTML Translation]
        State[React State & Auth Context]
        HTTP[API Client - Axios / Fetch]
        UI --> State
        State --> HTTP
    end

    subgraph Application Tier [Backend: Python + FastAPI]
        Router[FastAPI Routers /api/v1]
        Security[JWT Auth & RBAC Security Middleware]
        ServiceLayer[Business Logic & Price Calculation Engine]
        Repo[SQLAlchemy 2.0 ORM Repositories]
        
        Router --> Security
        Security --> ServiceLayer
        ServiceLayer --> Repo
    end

    subgraph Persistence Tier [Database: MySQL]
        DB[(banana_brothers_db - User: second_user)]
        Workbench[MySQL Workbench Management]
        Repo --> DB
        Workbench -.-> DB
    end

    HTTP -->|JSON over REST / HTTP| Router
```

- **Presentation Tier (React.js)**: Component-driven Single Page Application built in JavaScript/JSX using Vite. Directly translates the 12 HTML prototypes from `_bmad/New Pro` into modular React components while preserving 100% of their existing UI, classes, vanilla CSS, and interactions.
- **Application Tier (FastAPI)**: High-performance asynchronous REST API in Python 3.11+. Coordinates validation (Pydantic v2), secure role-based access control (JWT/bcrypt), live pricing recalculation, and database operations.
- **Persistence Tier (MySQL)**: ACID-compliant relational storage in MySQL 8.0+, managed via MySQL Workbench. Accessible through user credentials `second_user:gowtham2003`.

---

## 2. Invariants & Rules (Architectural Decisions)

### AD-1 [ADOPTED] — Strict 1:1 HTML-to-React UI Preservation (Zero Visual Drift)
- **Binds:** All React components and styles (`client/src/components/*`, `client/src/pages/*`)
- **Prevents:** Visual regression, modified styling, re-arranged DOM trees, or rewritten CSS.
- **Rule:** Every existing HTML page from `_bmad/New Pro` maps directly to a React page component. All CSS rules, class names, hover effects (e.g., left-to-right underline animation, card translations), inline SVGs, layout dimensions, and assets (`bb.jpeg`, `bg_blue.png`) must be preserved identically without adding external CSS frameworks (Tailwind/Bootstrap are banned).

### AD-2 [ADOPTED] — Pure JavaScript/JSX Runtime (No TypeScript)
- **Binds:** Frontend build configuration and codebase
- **Prevents:** TypeScript configuration overhead and tooling friction.
- **Rule:** The frontend MUST be authored purely in `.js` and `.jsx`. Bundling is managed via Vite with standard React plugins (`@vitejs/plugin-react`).

### AD-3 [ADOPTED] — FastAPI REST API Standard & JSON Envelope
- **Binds:** Application tier (`server/app/api/v1/*`)
- **Prevents:** Inconsistent HTTP contracts, non-standard error structures, and transport mismatches.
- **Rule:** All endpoints live under `/api/v1/`. Request and response payloads are strictly validated using Pydantic v2 schemas. Errors return standardized RFC-7807 shapes: `{"detail": "Error description", "code": "ERROR_CODE"}`. Cross-Origin Resource Sharing (CORS) is enabled for the Vite client (`http://localhost:5173`).

### AD-4 [ADOPTED] — Relational Integrity & Dedicated MySQL Database Role
- **Binds:** Database tier & ORM integration
- **Prevents:** SQL injection, unmanaged connection leaks, or schema divergence.
- **Rule:** Database name is `banana_brothers_db`. Backend connects via connection URI: `mysql+pymysql://second_user:gowtham2003@localhost:3306/banana_brothers_db`. Data access is managed via SQLAlchemy 2.0 declarative models with PyMySQL driver and pooled sessions.

### AD-5 [ADOPTED] — Stateless JWT & Role-Based Access Control (RBAC)
- **Binds:** Auth endpoints (`/api/v1/auth/*`), middleware, and protected routes
- **Prevents:** Session-hijacking, unauthorized booking tampering, or elevation of privilege.
- **Rule:** Passwords must be hashed using `bcrypt` (Passlib). Authentication issues a signed HMAC-SHA256 JWT access token carrying `sub` (user ID), `email`, and `role` (`CUSTOMER`, `ADMIN`). Protected routes enforce role verification using FastAPI's dependency injection (`Depends(get_current_user)`, `Depends(require_admin)`).

### AD-6 [ADOPTED] — Calculation Authority & Optimistic Client Rendering
- **Binds:** Booking price calculation (`FR-6`, `FR-7`, `High.html`, `Mediam.html`, `Low.html`)
- **Prevents:** Price tampering or inconsistencies between client quotation and stored orders.
- **Rule:** The React booking form mirrors the prototype's client-side dynamic calculation (`diffDays * base + sum(needs)`) for instant UI feedback. However, upon order submission, the FastAPI backend independently recalculates the exact amount based on database pricing rules before committing the transaction.

### AD-7 [ADOPTED] — Dynamic Data Hydration for Services & Packages
- **Binds:** `Services.jsx`, `Packages.jsx`, and configurator pages
- **Prevents:** Hardcoded static text drift between database records and UI cards.
- **Rule:** The 12 services and 3 package tiers are seeded into MySQL from prototype specs. React components fetch catalog data from `/api/v1/services` and `/api/v1/packages` on mount with fallback to prototype defaults if offline.

---

## 3. Consistency Conventions

| Concern | Convention | Example / Specification |
|---|---|---|
| **Frontend Components** | PascalCase filenames and identifiers | `Navbar.jsx`, `ServiceCard.jsx`, `HighBooking.jsx` |
| **Backend Files & Variables**| Snake_case for Python modules and variables | `booking_service.py`, `total_amount`, `get_db()` |
| **Database Entities** | Plural snake_case table names, snake_case columns | `users`, `bookings`, `booking_add_ons`, `created_at` |
| **API Endpoints** | Kebab-case plural nouns under `/api/v1` | `GET /api/v1/event-packages`, `POST /api/v1/bookings` |
| **Identifiers** | Auto-increment unsigned integers for DB PKs | `id BIGINT AUTO_INCREMENT PRIMARY KEY` |
| **Booking Reference Code** | Hex/alphanumeric unique string prefix | `BB-2026-XXXX` generated upon order creation |
| **Date & Time Formats** | ISO 8601 strings for API payload dates | `"2026-10-15"`, `"10:00:00"` |
| **Currency** | Integer Indian Rupees (INR) | Stored as `DECIMAL(12, 2)` or `INT`, rendered as `₹ 1,50,000` |

---

## 4. Technology Stack Seed

| Layer / Technology | Role / Purpose | Pinned Version | Configuration / Parameters |
|---|---|---|---|
| **React.js** | Frontend UI Framework | `18.2.0` | JavaScript/JSX, functional components, hooks |
| **Vite** | Frontend Build Tool & Dev Server | `5.1.0+` | Port `5173`, proxy configured to FastAPI backend |
| **React Router DOM** | Client-Side Routing | `6.22.0+` | History navigation matching existing HTML pages |
| **Axios** | HTTP API Client | `1.6.0+` | Centralized instance with JWT Bearer interceptor |
| **Python** | Backend Language | `3.11+` | Async execution, typed annotations |
| **FastAPI** | REST API Framework | `0.110.0+` | Uvicorn ASGI server on port `8000` |
| **Pydantic** | Request/Response Data Validation | `2.6.0+` | Strict schema serialization |
| **SQLAlchemy** | ORM & Query Builder | `2.0.28+` | Declarative mapping, session pooling |
| **PyMySQL** | MySQL Database Driver | `1.1.0+` | Pure Python DBAPI driver for MySQL |
| **Passlib (bcrypt)** | Cryptographic Password Hashing | `1.7.4` | Salted password verification |
| **PyJWT** | JWT Token Encoding & Verification | `2.8.0+` | HS256 algorithm, expiry handling |
| **MySQL Server** | Relational Database Engine | `8.0+` | Port `3306`, InnoDB engine, UTF-8 collation |
| **MySQL Workbench** | Database Administration GUI | `8.0+` | Schema visual inspection & query execution |

---

## 5. Structural Seed & Folder Hierarchy

```text
Event website/
├── client/                                 # React.js Single Page Application (JS/JSX)
│   ├── public/
│   │   ├── bb.jpeg                         # Brand logo image
│   │   ├── bg_blue.png                     # Blueprint background texture
│   │   └── favicon.ico
│   ├── src/
│   │   ├── assets/                         # Static images and icons
│   │   ├── components/                     # Reusable UI components from HTML prototypes
│   │   │   ├── Navbar.jsx                  # Navbar from Navbar.html
│   │   │   ├── Footer.jsx                  # Footer from Footer.html
│   │   │   ├── ServiceCard.jsx             # Card from Services.html
│   │   │   ├── PackageRow.jsx              # Full-width card from Pakages.html
│   │   │   ├── EventCard.jsx               # Dashboard card from Myevents.html
│   │   │   └── Toast.jsx                   # msg-box notification from Register/Login
│   │   ├── pages/                          # Page views matching New Pro HTML files
│   │   │   ├── Home.jsx                    # Home.html
│   │   │   ├── Services.jsx                # Services.html
│   │   │   ├── Packages.jsx                # Pakages.html
│   │   │   ├── HighBooking.jsx             # High.html (Royal Luxury 2-step booking)
│   │   │   ├── MediumBooking.jsx           # Mediam.html (Standard Classic 2-step booking)
│   │   │   ├── LowBooking.jsx              # Low.html (Budget Friendly 2-step booking)
│   │   │   ├── MyEvents.jsx                # Myevents.html
│   │   │   ├── Login.jsx                   # Login.html
│   │   │   ├── Register.jsx                # Register.html
│   │   │   └── ForgotPassword.jsx          # Forget.html
│   │   ├── context/
│   │   │   └── AuthContext.jsx             # User auth state, token storage, login/logout
│   │   ├── services/
│   │   │   ├── api.js                      # Axios instance with auth headers
│   │   │   ├── authService.js              # Auth API calls
│   │   │   ├── bookingService.js           # Order submission & retrieval
│   │   │   └── catalogService.js           # Services and Packages fetch
│   │   ├── styles/                         # Extracted vanilla CSS stylesheets
│   │   │   ├── common.css                  # Typography, reset, bg_blue.png pattern
│   │   │   ├── navbar.css                  # Navbar styling & underline animation
│   │   │   ├── footer.css                  # Footer layout
│   │   │   ├── home.css                    # Hero & floating cards
│   │   │   ├── catalog.css                 # Services & Packages grids
│   │   │   ├── booking.css                 # Slider, 2-step form, checkboxes, price summary
│   │   │   └── auth.css                    # Compact centered login/register cards
│   │   ├── App.jsx                         # React router setup & layouts
│   │   ├── main.jsx                        # React entry point
│   │   └── index.html                      # HTML root template
│   ├── package.json
│   └── vite.config.js
│
└── server/                                 # Python FastAPI Application
    ├── app/
    │   ├── api/
    │   │   └── v1/
    │   │       ├── endpoints/
    │   │       │   ├── auth.py             # /api/v1/auth (login, register, otp, reset)
    │   │       │   ├── services.py         # /api/v1/services (catalog & filters)
    │   │       │   ├── packages.py         # /api/v1/packages (tier configurations)
    │   │       │   ├── bookings.py         # /api/v1/bookings (2-step submission & calculation)
    │   │       │   └── events.py           # /api/v1/events (customer My Events dashboard)
    │   │       └── router.py               # Aggregated v1 API router
    │   ├── core/
    │   │   ├── config.py                   # Pydantic Settings (DB URL, JWT Secret)
    │   │   ├── database.py                 # SQLAlchemy engine, sessionmaker, get_db dependency
    │   │   └── security.py                 # Password hash, JWT verify, current user extractor
    │   ├── models/                         # SQLAlchemy ORM Entities
    │   │   ├── user.py                     # User table model
    │   │   ├── service.py                  # Service table model
    │   │   ├── package.py                  # Package and AddOn models
    │   │   └── booking.py                  # Booking and BookingItem models
    │   ├── schemas/                        # Pydantic Schemas
    │   │   ├── auth.py                     # Login, Register, OTP schemas
    │   │   ├── service.py                  # Service response schemas
    │   │   ├── package.py                  # Package response schemas
    │   │   └── booking.py                  # Booking create, calculate, response schemas
    │   ├── services/                       # Business Logic Layer
    │   │   ├── auth_service.py             # User registration & token generation
    │   │   └── pricing_engine.py           # Multi-day and add-on price calculation
    │   └── main.py                         # FastAPI application factory & CORS setup
    ├── db/
    │   ├── schema.sql                      # DDL script for MySQL Workbench initialization
    │   └── seed.sql                        # Default catalog seed data
    ├── requirements.txt                    # Python dependencies
    └── run.py                              # Local dev runner (uvicorn app.main:app)
```

---

## 6. Database Architecture & Relational Entity Model

```mermaid
erDiagram
    USERS ||--o{ BOOKINGS : places
    PACKAGES ||--o{ BOOKINGS : "booked under"
    BOOKINGS ||--o{ BOOKING_ADD_ONS : contains
    SERVICES ||--o{ BOOKING_ADD_ONS : "references service"

    USERS {
        bigint id PK
        string username UK
        string email UK
        string password_hash
        string first_name
        string last_name
        int age
        string role "CUSTOMER | ADMIN"
        boolean is_verified
        datetime created_at
    }

    PACKAGES {
        bigint id PK
        string slug UK "high | medium | low"
        string name "Royal Luxury | Standard Classic | Budget Friendly"
        decimal starting_price
        decimal base_price
        string description
        string image_url
        string badge_class
    }

    SERVICES {
        bigint id PK
        string name "Wedding Planners, Catering, etc."
        string category "Weddings | Birthdays | Corporate | Entertainment"
        string description
        decimal starting_price
        string price_unit "flat | plate"
        string image_url
    }

    BOOKINGS {
        bigint id PK
        string booking_reference UK "BB-2026-XXXX"
        bigint user_id FK
        bigint package_id FK
        string full_name
        string mobile_no
        string alt_mobile_no
        string email
        string function_category "Thirumanam, Reception, etc."
        string district "Chennai, Madurai, etc."
        string place_area
        text full_address
        string pincode
        date from_date
        date to_date
        time from_time
        time to_time
        int duration_days
        text map_location_url
        decimal calculated_base_amount
        decimal total_amount
        string status "UPCOMING | COMPLETED | CANCELLED"
        datetime created_at
    }

    BOOKING_ADD_ONS {
        bigint id PK
        bigint booking_id FK
        string need_name "Food, Catering, DJ, etc."
        decimal price
    }
```

### MySQL Workbench Initialization DDL (`server/db/schema.sql`)

```sql
-- Banana Brothers Database Initialization
-- Execute in MySQL Workbench under user: second_user
CREATE DATABASE IF NOT EXISTS banana_brothers_db
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE banana_brothers_db;

-- 1. Users Table
CREATE TABLE IF NOT EXISTS users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    role ENUM('CUSTOMER', 'ADMIN') DEFAULT 'CUSTOMER',
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2. Packages Table
CREATE TABLE IF NOT EXISTS packages (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    slug VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(150) NOT NULL,
    starting_price DECIMAL(12, 2) NOT NULL,
    base_price DECIMAL(12, 2) NOT NULL,
    description TEXT,
    image_url VARCHAR(500),
    badge_class VARCHAR(50)
) ENGINE=InnoDB;

-- 3. Services Table
CREATE TABLE IF NOT EXISTS services (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category ENUM('Weddings', 'Birthdays', 'Corporate', 'Entertainment') NOT NULL,
    description TEXT,
    starting_price DECIMAL(12, 2) NOT NULL,
    price_unit VARCHAR(50) DEFAULT 'flat',
    image_url VARCHAR(500)
) ENGINE=InnoDB;

-- 4. Bookings Table
CREATE TABLE IF NOT EXISTS bookings (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    booking_reference VARCHAR(50) NOT NULL UNIQUE,
    user_id BIGINT NULL,
    package_id BIGINT NOT NULL,
    full_name VARCHAR(150) NOT NULL,
    mobile_no VARCHAR(15) NOT NULL,
    alt_mobile_no VARCHAR(15) NULL,
    email VARCHAR(150) NOT NULL,
    function_category VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL,
    place_area VARCHAR(150) NOT NULL,
    full_address TEXT NOT NULL,
    pincode VARCHAR(10) NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    from_time TIME NOT NULL,
    to_time TIME NOT NULL,
    duration_days INT DEFAULT 1,
    map_location_url TEXT NOT NULL,
    calculated_base_amount DECIMAL(12, 2) NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    status ENUM('UPCOMING', 'COMPLETED', 'CANCELLED') DEFAULT 'UPCOMING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_booking_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
    CONSTRAINT fk_booking_package FOREIGN KEY (package_id) REFERENCES packages(id)
) ENGINE=InnoDB;

-- 5. Booking Add-Ons Table
CREATE TABLE IF NOT EXISTS booking_add_ons (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    booking_id BIGINT NOT NULL,
    need_name VARCHAR(100) NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    CONSTRAINT fk_addon_booking FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE
) ENGINE=InnoDB;
```

---

## 7. REST API Endpoints Contract

| Method | Endpoint | Description | Auth Required | Request Payload | Response Body |
|---|---|---|---|---|---|
| `POST` | `/api/v1/auth/register` | Register new customer account | No | `RegisterRequest` (first/last name, username, email, age, password, otp) | `UserResponse` + token |
| `POST` | `/api/v1/auth/login` | Authenticate customer or admin | No | `LoginRequest` (username/email, password) | `TokenResponse` (`access_token`, user object) |
| `POST` | `/api/v1/auth/send-otp` | Request simulation / email OTP | No | `{"email": "user@example.com"}` | `{"message": "OTP sent", "success": true}` |
| `POST` | `/api/v1/auth/verify-otp` | Verify 6-digit OTP code | No | `{"email": "user@example.com", "otp": "123456"}` | `{"verified": true}` |
| `POST` | `/api/v1/auth/forgot-password`| Reset account password | No | `{"email": "...", "otp": "...", "new_password": "..."}` | `{"message": "Password reset successful"}` |
| `GET` | `/api/v1/services` | Retrieve 12 catalog services | No | Query: `?category=Weddings` (optional) | List of `ServiceResponse` objects |
| `GET` | `/api/v1/packages` | Retrieve 3 package tiers | No | None | List of `PackageResponse` objects |
| `POST` | `/api/v1/bookings/calculate` | Recalculate price dynamically | No | `BookingEstimateRequest` (tier, needs, from_date, to_date) | `{"duration_days": 2, "estimated_amount": 350000}` |
| `POST` | `/api/v1/bookings` | Submit final 2-step booking order | Optional (Auto-links if logged in) | `BookingCreateRequest` (Step 1 + Step 2 fields) | `BookingDetailResponse` with reference code |
| `GET` | `/api/v1/events/my-events` | Customer dashboard bookings | Yes (`CUSTOMER`) | Header: `Authorization: Bearer <token>` | List of user's `BookingSummaryResponse` cards |

---

## 8. Frontend ↔ FastAPI ↔ MySQL Data Flow Walkthrough

```mermaid
sequenceDiagram
    autonumber
    actor Customer
    participant React as React SPA (Client)
    participant FastAPI as FastAPI Backend (Server)
    participant MySQL as MySQL Database (second_user)

    Customer->>React: Selects "Royal Luxury" on Packages.jsx
    React->>React: Routes to HighBooking.jsx (Step 1)
    Customer->>React: Toggles "Food" (+40k) & "DJ Music" (+20k)
    React->>FastAPI: POST /api/v1/bookings/calculate (tier, needs, dates)
    FastAPI-->>React: {"total": 210000, "days": 1}
    React->>React: Updates #totalPriceDisplay smoothly
    Customer->>React: Clicks "Next Step" (Validates Step 1)
    React->>React: Reveals Step 2 with fadeIn & scrollIntoView
    Customer->>React: Selects District, Address, Dates & Map link
    Customer->>React: Clicks "BOOK YOUR ORDER NOW"
    React->>FastAPI: POST /api/v1/bookings (Full payload)
    FastAPI->>FastAPI: Authenticates user token (if present) & validates schema
    FastAPI->>FastAPI: Re-verifies price calculation via pricing_engine.py
    FastAPI->>MySQL: INSERT INTO bookings, INSERT INTO booking_add_ons
    MySQL-->>FastAPI: Committed transaction (ID: 101, Ref: BB-2026-9481)
    FastAPI-->>React: 201 Created (Booking details & reference code)
    React->>Customer: Displays order success alert with reference code
    Customer->>React: Clicks "My Events"
    React->>FastAPI: GET /api/v1/events/my-events (Bearer token)
    FastAPI->>MySQL: SELECT * FROM bookings WHERE user_id = :id
    MySQL-->>FastAPI: Result rows
    FastAPI-->>React: JSON array of booking cards
    React->>Customer: Renders MyEvents.jsx cards with UPCOMING badges
```

---

## 9. Capability → Architecture Mapping

| PRD Capability | Source HTML File | React Component (`client/`) | FastAPI Router (`server/`) | Database Table (`MySQL`) |
|---|---|---|---|---|
| **FR-1: Global Navbar** | `Navbar.html` | `components/Navbar.jsx` | `endpoints/services.py` | — |
| **FR-2: Search** | `Navbar.html` | `components/Navbar.jsx` | `endpoints/services.py?q=` | `services`, `packages` |
| **FR-3: Hero & CTAs** | `Home.html` | `pages/Home.jsx` | — | — |
| **FR-4: 12 Services & Filters** | `Services.html` | `pages/Services.jsx`, `components/ServiceCard.jsx` | `endpoints/services.py` | `services` |
| **FR-5: 3 Tier Packages** | `Pakages.html` | `pages/Packages.jsx`, `components/PackageRow.jsx` | `endpoints/packages.py` | `packages` |
| **FR-6: Booking Step 1** | `High/Mediam/Low.html` | `pages/HighBooking.jsx`, `MediumBooking.jsx`, `LowBooking.jsx` | `endpoints/bookings.py` | `booking_add_ons` |
| **FR-7: Booking Step 2** | `High/Mediam/Low.html` | `pages/HighBooking.jsx`, etc. | `endpoints/bookings.py` | `bookings` |
| **FR-8: My Events Dashboard** | `Myevents.html` | `pages/MyEvents.jsx`, `components/EventCard.jsx` | `endpoints/events.py` | `bookings` |
| **FR-9: Register + OTP** | `Register.html` | `pages/Register.jsx` | `endpoints/auth.py` | `users` |
| **FR-10: Login & Forgot Pass** | `Login.html`, `Forget.html`| `pages/Login.jsx`, `pages/ForgotPassword.jsx` | `endpoints/auth.py` | `users` |
| **FR-11: Global Footer** | `Footer.html` | `components/Footer.jsx` | — | — |

---

## 10. Deferred Decisions

1. **Production Deployment & Reverse Proxy**: Docker Compose containerization and Nginx reverse proxy configuration are deferred to the deployment hardening sprint.
2. **Third-Party SMS Gateway Binding**: Replacing simulated OTP verification with Twilio/Gupshup Indian DLT API is deferred to v2 per PRD non-goals.
3. **Automated Payment Gateway**: Razorpay/UPI deep link checkout is deferred to v1.1 per PRD non-goals.
