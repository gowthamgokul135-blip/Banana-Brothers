import axios from 'axios';

const api = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json'
  }
});

// Intercept requests to attach JWT token if present
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('bb_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, (error) => Promise.reject(error));

export const authAPI = {
  login: (data) => api.post('/auth/login', data),
  register: (data) => api.post('/auth/register', data),
  getMe: () => api.get('/auth/me'),
  sendOTP: (email) => api.post('/auth/send-otp', { email }),
  verifyOTP: (email, otp) => api.post('/auth/verify-otp', { email, otp }),
  forgotPassword: (data) => api.post('/auth/forgot-password', data),
};

export const catalogAPI = {
  getServices: (category, query) => {
    let url = '/services';
    const params = new URLSearchParams();
    if (category && category !== 'All Services') params.append('category', category);
    if (query) params.append('q', query);
    const queryString = params.toString();
    return api.get(queryString ? `${url}?${queryString}` : url);
  },
  getPackages: () => api.get('/packages'),
  getPackageBySlug: (slug) => api.get(`/packages/${slug}`),
};

export const bookingAPI = {
  calculate: (data) => api.post('/bookings/calculate', data),
  create: (data) => api.post('/bookings', data),
  getBooking: (idOrRef) => api.get(`/bookings/${idOrRef}`),
  getMyEvents: () => api.get('/events/my-events'),
};

export const adminAPI = {
  getStats: () => api.get('/admin/stats'),
  getBookings: (status, query) => {
    let url = '/admin/bookings';
    const params = new URLSearchParams();
    if (status && status !== 'ALL') params.append('status', status);
    if (query) params.append('q', query);
    const queryString = params.toString();
    return api.get(queryString ? `${url}?${queryString}` : url);
  },
  getBookingDetail: (id) => api.get(`/admin/bookings/${id}`),
  updateStatus: (id, status) => api.patch(`/admin/bookings/${id}/status`, { status }),
  getUsers: () => api.get('/admin/users'),
};

export default api;
