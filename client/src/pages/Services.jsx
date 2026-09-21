import React, { useState, useEffect } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { catalogAPI } from '../services/api';

const DEFAULT_SERVICES = [
  {
    id: 1,
    name: 'Wedding Planners',
    category: 'Weddings',
    description: 'Complete end-to-end wedding management with traditional arrangements, themed setups, and seamless coordination.',
    starting_price: 150000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80',
    target_package: 'high'
  },
  {
    id: 2,
    name: 'Reception & Engagement',
    category: 'Weddings',
    description: 'Grand ring ceremony setups, luxury stage entrances, floral backdrops, and complete guest hospitality.',
    starting_price: 80000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80',
    target_package: 'medium'
  },
  {
    id: 3,
    name: 'Corporate Events',
    category: 'Corporate',
    description: 'Professional business conferences, product launches, annual company meets, and team celebrations.',
    starting_price: 75000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=600&q=80',
    target_package: 'medium'
  },
  {
    id: 4,
    name: 'Cultural Events',
    category: 'Corporate',
    description: 'Vibrant college fest execution, traditional performance stages, sound systems, and lighting management.',
    starting_price: 50000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1465847899084-d164df4dedc6?auto=format&fit=crop&w=600&q=80',
    target_package: 'medium'
  },
  {
    id: 5,
    name: 'Birthday Parties',
    category: 'Birthdays',
    description: 'Customized themed birthday setups for children and adults with fun activities and decorative cake tables.',
    starting_price: 25000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=600&q=80',
    target_package: 'low'
  },
  {
    id: 6,
    name: 'Baby Shower',
    category: 'Birthdays',
    description: 'Traditional and modern baby shower themes, decorated cradle setups, photo booths, and event management.',
    starting_price: 35000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?auto=format&fit=crop&w=600&q=80',
    target_package: 'low'
  },
  {
    id: 7,
    name: 'Surprise Events',
    category: 'Entertainment',
    description: 'Memorable romantic proposals, anniversary surprises, secret birthday celebrations, and custom setups.',
    starting_price: 15000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=600&q=80',
    target_package: 'low'
  },
  {
    id: 8,
    name: 'Stage Decorations',
    category: 'Weddings',
    description: 'Elegant flower arc stages, custom balloon backdrops, ambient lighting, and modern thematic decorations.',
    starting_price: 20000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1527529482837-4698179dc6ce?auto=format&fit=crop&w=600&q=80',
    target_package: 'medium'
  },
  {
    id: 9,
    name: 'Catering Services',
    category: 'Weddings',
    description: 'Delicious vegetarian and non-vegetarian buffet spreads, traditional banana leaf feasts, and live counters.',
    starting_price: 250,
    price_unit: 'plate',
    image_url: 'https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=600&q=80',
    target_package: 'high'
  },
  {
    id: 10,
    name: 'Photography',
    category: 'Entertainment',
    description: 'High-resolution candid photography, traditional portraits, pre-wedding photoshoots, and premium albums.',
    starting_price: 30000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=600&q=80',
    target_package: 'medium'
  },
  {
    id: 11,
    name: 'Videography',
    category: 'Entertainment',
    description: 'Cinematic 4K video coverage, aerial drone shots, live event streaming setups, and highlight editing.',
    starting_price: 40000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=600&q=80',
    target_package: 'high'
  },
  {
    id: 12,
    name: 'Entertainment & DJ',
    category: 'Entertainment',
    description: 'High-energy live DJ performances, concert-grade sound setups, LED dance floors, and event anchors.',
    starting_price: 18000,
    price_unit: 'flat',
    image_url: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=600&q=80',
    target_package: 'medium'
  }
];

export default function Services() {
  const [searchParams] = useSearchParams();
  const searchKeyword = searchParams.get('q') || '';
  const [activeCategory, setActiveCategory] = useState('All Services');
  const [services, setServices] = useState(DEFAULT_SERVICES);

  const categories = ['All Services', 'Weddings', 'Birthdays', 'Corporate', 'Entertainment'];

  useEffect(() => {
    catalogAPI.getServices(activeCategory, searchKeyword)
      .then((res) => {
        if (res.data && res.data.length > 0) {
          setServices(res.data);
        }
      })
      .catch(() => {
        // Fallback filter locally
        let list = DEFAULT_SERVICES;
        if (activeCategory !== 'All Services') {
          list = list.filter((s) => s.category.toLowerCase() === activeCategory.toLowerCase());
        }
        if (searchKeyword) {
          const k = searchKeyword.toLowerCase();
          list = list.filter((s) => s.name.toLowerCase().includes(k) || s.description.toLowerCase().includes(k));
        }
        setServices(list);
      });
  }, [activeCategory, searchKeyword]);

  return (
    <main className="services-section">
      {/* Header */}
      <div className="header-container">
        <span className="badge">What We Offer</span>
        <h1 className="main-title">Our Professional Services</h1>
        <p className="subtitle">
          Whatever your event may be, from stage decorations to premium catering, we execute everything to perfection.
        </p>
      </div>

      {/* Filter Buttons */}
      <div className="filters-container">
        {categories.map((cat) => (
          <button
            key={cat}
            type="button"
            className={`filter-btn ${activeCategory === cat ? 'active' : ''}`}
            onClick={() => setActiveCategory(cat)}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Cards Grid (3 Columns) */}
      <div className="services-grid">
        {services.map((service) => (
          <div className="service-card" key={service.id}>
            <img src={service.image_url} alt={service.name} className="service-card-image" />
            <div className="service-card-body">
              <h3 className="service-card-title">{service.name}</h3>
              <p className="service-card-desc">{service.description}</p>
              <div className="service-card-footer">
                <div>
                  <span className="price-label">Starting from</span>
                  <span className="price-val">
                    ₹{Number(service.starting_price).toLocaleString('en-IN')}{' '}
                    {service.price_unit === 'plate' ? '/ plate' : ''}
                  </span>
                </div>
                <Link to={`/packages/${service.target_package || 'medium'}`} className="book-btn">
                  Book Now
                </Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
