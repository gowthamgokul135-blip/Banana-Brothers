import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { authAPI } from '../services/api';

export default function ForgotPassword() {
  const [email, setEmail] = useState('');
  const [otp, setOtp] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [msg, setMsg] = useState('');
  const [otpSent, setOtpSent] = useState(false);
  const [otpVerified, setOtpVerified] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const showToast = (text) => {
    setMsg(text);
    setTimeout(() => setMsg(''), 2500);
  };

  const handleSendOTP = async () => {
    if (!email) {
      showToast('Please enter email address first');
      return;
    }
    try {
      await authAPI.sendOTP(email);
      setOtpSent(true);
      showToast('OTP sent to your email!');
    } catch (err) {
      showToast(err.response?.data?.detail || 'Failed to send OTP');
    }
  };

  const handleVerifyOTP = async () => {
    if (!otp) {
      showToast('Please enter the OTP');
      return;
    }
    try {
      await authAPI.verifyOTP(email, otp);
      setOtpVerified(true);
      showToast('OTP verified successfully!');
    } catch (err) {
      showToast(err.response?.data?.detail || 'Invalid or expired OTP');
    }
  };

  const handleResetPassword = async (e) => {
    e.preventDefault();

    if (newPassword !== confirmPassword) {
      showToast('Passwords do not match');
      return;
    }

    setLoading(true);
    try {
      await authAPI.forgotPassword({
        email,
        otp,
        new_password: newPassword
      });
      showToast('Password reset successful!');
      setTimeout(() => navigate('/login'), 800);
    } catch (err) {
      const detail = err.response?.data?.detail || 'Password reset failed. Please try again.';
      showToast(detail);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-page-wrapper">
      {msg && <div className="msg-box">{msg}</div>}

      <div className="forgot-container">
        <h1 className="forgot-title">Forgot Password</h1>

        <form className="auth-form" onSubmit={handleResetPassword}>
          {/* Email with Send OTP */}
          <div className="input-group">
            <div className="input-with-action">
              <input
                type="email"
                className="input-field-auth"
                placeholder="Email address"
                required
                autoComplete="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <button
                type="button"
                className="action-btn"
                onClick={handleSendOTP}
              >
                {otpSent ? 'Resend' : 'Send OTP'}
              </button>
            </div>
          </div>

          {/* OTP with Verify */}
          <div className="input-group">
            <div className="input-with-action">
              <input
                type="text"
                className="input-field-auth"
                placeholder="Enter OTP"
                maxLength="6"
                required
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
              />
              <button
                type="button"
                className="action-btn"
                onClick={handleVerifyOTP}
              >
                {otpVerified ? '✓ Verified' : 'Verify'}
              </button>
            </div>
          </div>

          {/* New Password */}
          <div className="input-group">
            <input
              type="password"
              className="input-field-auth"
              placeholder="New password"
              required
              autoComplete="new-password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            />
          </div>

          {/* Confirm Password */}
          <div className="input-group">
            <input
              type="password"
              className="input-field-auth"
              placeholder="Confirm password"
              required
              autoComplete="new-password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          </div>

          {/* Link Row */}
          <div className="links-row">
            <Link to="/login" className="link-item">
              Remembered password? Login
            </Link>
          </div>

          {/* Submit Button */}
          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? 'Resetting...' : 'Reset Password'}
          </button>
        </form>
      </div>
    </div>
  );
}
