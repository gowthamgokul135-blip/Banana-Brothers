import React from 'react';
import { Link } from 'react-router-dom';

export default function Packages() {
  return (
    <main className="packages-container">
      {/* Main Header */}
      <div className="header-container">
        <span className="badge">Pricing Plans</span>
        <h1 className="main-title">Event Packages</h1>
        <p className="subtitle">
          Explore our High, Medium, and Low budget event packages with complete arrangements.
        </p>
      </div>

      {/* 1. HIGH PACKAGE */}
      <div className="package-row">
        <div className="full-width-card">
          <div className="package-image-container">
            <img
              src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80"
              alt="High Package"
              className="package-card-image"
            />
            <span className="tier-badge badge-high">High Package</span>
          </div>
          <div className="package-card-body">
            <div className="package-card-info">
              <h3 className="package-card-title">Royal Luxury Package</h3>
              <p className="package-card-desc">
                Grand stage decor, premium imported floral setups, 4K cinematic videography, drone coverage, and lavish multi-course buffet catering.
              </p>
            </div>
            <div className="package-card-action">
              <div>
                <span className="price-label">Starting from</span>
                <span className="price-val">₹3,50,000</span>
              </div>
              <Link to="/packages/high" className="book-btn">
                Book Package
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* 2. MEDIUM PACKAGE */}
      <div className="package-row">
        <div className="full-width-card">
          <div className="package-image-container">
            <img
              src="https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=1200&q=80"
              alt="Medium Package"
              className="package-card-image"
            />
            <span className="tier-badge badge-medium">Medium Package</span>
          </div>
          <div className="package-card-body">
            <div className="package-card-info">
              <h3 className="package-card-title">Standard Classic Package</h3>
              <p className="package-card-desc">
                Elegant flower arc background, candid photography, professional sound & DJ setup, theme cake table, and quality catering service.
              </p>
            </div>
            <div className="package-card-action">
              <div>
                <span className="price-label">Starting from</span>
                <span className="price-val">₹1,20,000</span>
              </div>
              <Link to="/packages/medium" className="book-btn">
                Book Package
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* 3. LOW PACKAGE */}
      <div className="package-row">
        <div className="full-width-card">
          <div className="package-image-container">
            <img
              src="https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=1200&q=80"
              alt="Low Package"
              className="package-card-image"
            />
            <span className="tier-badge badge-low">Low Package</span>
          </div>
          <div className="package-card-body">
            <div className="package-card-info">
              <h3 className="package-card-title">Budget Friendly Package</h3>
              <p className="package-card-desc">
                Minimalist stage backdrop setup, balloon arches, focus LED lighting, and basic audio equipment suitable for small home events.
              </p>
            </div>
            <div className="package-card-action">
              <div>
                <span className="price-label">Starting from</span>
                <span className="price-val">₹25,000</span>
              </div>
              <Link to="/packages/low" className="book-btn">
                Book Package
              </Link>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
