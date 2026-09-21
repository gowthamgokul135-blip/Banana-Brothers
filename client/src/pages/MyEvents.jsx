import React, { useState, useEffect } from 'react';
import { bookingAPI } from '../services/api';
import { useAuth } from '../context/AuthContext';

const DEFAULT_EVENTS = [
  {
    id: 1,
    title: 'Grand Royal Wedding',
    date: '15 Nov 2026',
    location: 'Chennai, Tamil Nadu',
    description: 'Full traditional wedding setup with imported floral backdrop, cinematic 4K videography, and lavish multi-course feast.',
    image_url: 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80',
    status: 'UPCOMING',
    status_class: 'status-upcoming',
    booking_reference: 'BB-2026-DEMO1'
  },
  {
    id: 2,
    title: 'Corporate Annual Gala',
    date: '02 Dec 2026',
    location: 'Coimbatore, Tamil Nadu',
    description: 'Executive conference setup with high-end audio-visual systems, ambient lighting, and executive catering buffet.',
    image_url: 'https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=600&q=80',
    status: 'UPCOMING',
    status_class: 'status-upcoming',
    booking_reference: 'BB-2026-DEMO2'
  },
  {
    id: 3,
    title: '1st Birthday Celebration',
    date: '24 Aug 2026',
    location: 'Madurai, Tamil Nadu',
    description: 'Themed balloon arch decorations, custom cake table arrangement, sound system, and fun entertainment activities.',
    image_url: 'https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=600&q=80',
    status: 'COMPLETED',
    status_class: 'status-completed',
    booking_reference: 'BB-2026-DEMO3'
  }
];

export default function MyEvents() {
  const [events, setEvents] = useState(DEFAULT_EVENTS);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const { user } = useAuth();

  useEffect(() => {
    bookingAPI.getMyEvents()
      .then((res) => {
        if (res.data && res.data.length > 0) {
          const mapped = res.data.map((item) => ({
            ...item,
            status_class: item.status === 'COMPLETED' ? 'status-completed' : 'status-upcoming'
          }));
          setEvents(mapped);
        }
      })
      .catch(() => {
        // Fallback to default events
        setEvents(DEFAULT_EVENTS);
      });
  }, [user]);

  return (
    <main className="events-container">
      {/* Header Section */}
      <div className="header-container">
        <span className="badge">Your Bookings</span>
        <h1 className="main-title">My Events</h1>
        <p className="subtitle">
          View and manage all your booked events, active schedules, and past celebrations.
        </p>
      </div>

      {/* Grid - 3 Cards per Line */}
      <div className="events-grid">
        {events.map((ev) => (
          <div className="event-card" key={ev.id || ev.booking_reference}>
            <div className="card-image-wrap">
              <img src={ev.image_url || 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80'} alt={ev.title} className="card-image" />
              <span className={`status-tag ${ev.status_class || (ev.status === 'COMPLETED' ? 'status-completed' : 'status-upcoming')}`}>
                {ev.status || 'UPCOMING'}
              </span>
            </div>
            <div className="service-card-body">
              <span className="event-date">📅 {ev.date}</span>
              <h3 className="service-card-title">{ev.title}</h3>
              <p className="service-card-desc">{ev.description}</p>
              <div className="service-card-footer">
                <span className="location-info">📍 {ev.location}</span>
                <button
                  type="button"
                  className="view-btn"
                  onClick={() => setSelectedEvent(ev)}
                >
                  View Details
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Detail Modal */}
      {selectedEvent && (
        <div
          style={{
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100vw',
            height: '100vh',
            background: 'rgba(0,0,0,0.75)',
            backdropFilter: 'blur(8px)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 9999,
            padding: '20px'
          }}
          onClick={() => setSelectedEvent(null)}
        >
          <div
            style={{
              background: '#0f172a',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              borderRadius: '12px',
              padding: '26px',
              maxWidth: '520px',
              width: '100%',
              boxShadow: '0 16px 40px rgba(0,0,0,0.5)',
              color: '#fff'
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
              <h3 style={{ fontSize: '1.25rem', fontWeight: '700', color: '#fff' }}>{selectedEvent.title}</h3>
              <span style={{
                background: selectedEvent.status === 'COMPLETED' ? 'rgba(56, 161, 105, 0.2)' : 'rgba(221, 107, 32, 0.2)',
                color: selectedEvent.status === 'COMPLETED' ? '#68d391' : '#f6ad55',
                border: `1px solid ${selectedEvent.status === 'COMPLETED' ? '#38a169' : '#dd6b20'}`,
                padding: '3px 10px',
                borderRadius: '12px',
                fontSize: '0.78rem',
                fontWeight: '700'
              }}>
                {selectedEvent.status}
              </span>
            </div>

            {selectedEvent.booking_reference && (
              <div style={{ marginBottom: '14px', fontSize: '0.85rem', color: '#a0aec0' }}>
                Booking Ref: <strong style={{ color: '#63b3ed', fontFamily: 'monospace' }}>{selectedEvent.booking_reference}</strong>
              </div>
            )}

            <div style={{ background: 'rgba(255,255,255,0.04)', padding: '12px 16px', borderRadius: '8px', marginBottom: '14px' }}>
              <div style={{ fontSize: '0.88rem', marginBottom: '6px', color: '#e2e8f0' }}>
                <strong>📅 Date:</strong> {selectedEvent.date}
              </div>
              <div style={{ fontSize: '0.88rem', color: '#e2e8f0' }}>
                <strong>📍 Venue / District:</strong> {selectedEvent.location}
              </div>
            </div>

            <p style={{ fontSize: '0.9rem', color: '#cbd5e0', lineHeight: 1.5, marginBottom: '18px' }}>
              {selectedEvent.description}
            </p>

            {selectedEvent.total_amount && (
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', padding: '10px 14px', background: 'rgba(56, 161, 105, 0.1)', border: '1px solid rgba(56, 161, 105, 0.3)', borderRadius: '8px' }}>
                <span style={{ fontSize: '0.9rem', color: '#a0aec0' }}>Total Package Amount:</span>
                <span style={{ fontSize: '1.2rem', fontWeight: '800', color: '#68d391' }}>
                  ₹ {Number(selectedEvent.total_amount).toLocaleString('en-IN')}
                </span>
              </div>
            )}

            <button
              type="button"
              className="view-btn"
              style={{ width: '100%', padding: '10px', fontSize: '0.95rem', cursor: 'pointer', textAlign: 'center' }}
              onClick={() => setSelectedEvent(null)}
            >
              Close Details
            </button>
          </div>
        </div>
      )}
    </main>
  );
}
