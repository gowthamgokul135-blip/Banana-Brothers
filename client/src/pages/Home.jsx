import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <section className="hero-section">
      {/* Background Decorative Element */}
      <div className="bg-shape"></div>

      {/* Left Content */}
      <div className="hero-content">
        <span className="badge">Banana Brothers Events</span>
        <h1 className="hero-title">
          Crafting <span>Unforgettable</span> Experiences.
        </h1>
        <p className="hero-description">
          Elevate your celebrations with Banana Brothers. From bespoke premium packages to seamless online booking, we turn your special moments into unforgettable luxury experiences.
        </p>
        <div className="btn-group">
          <Link to="/packages" className="btn-primary">
            Explore Packages
          </Link>
          <Link to="/packages" className="btn-secondary">
            Book Event
          </Link>
        </div>
      </div>

      {/* Right Card with Linear Gradient Background */}
      <div className="hero-image-wrapper">


        <div className="image-container">
          <div className="card-inner-text">
            <h3>Banana Brothers</h3>
            <p>Making every moment magical & memorable.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
