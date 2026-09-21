---
title: Banana Brothers Events Platform
status: draft
created: 2026-09-20
updated: 2026-09-20
---

# PRD: Banana Brothers Events Platform

## 0. Document Purpose
This Product Requirement Document (PRD) defines the functional, experiential, and operational requirements for the **Banana Brothers Events Platform**. It serves engineering, UX design, product leadership, and business stakeholders. The specifications in this document are directly grounded in and reverse-engineered from the foundational HTML/CSS/JS prototype located in `_bmad/New Pro` (covering `Home.html`, `Navbar.html`, `Footer.html`, `Services.html`, `Pakages.html`, `High.html`, `Mediam.html`, `Low.html`, `Myevents.html`, `Login.html`, `Register.html`, and `Forget.html`).

---

## 1. Vision
Banana Brothers is an event management and celebration service operating across Tamil Nadu, India. The vision is to make memorable milestones—weddings, birthdays, corporate meets, and traditional family functions—effortless, transparent, and joyful to organize.

By combining an intuitive digital storefront, transparent multi-tier packages (Low, Medium, High), granular service customization, and direct booking logistics (spanning venue geolocation and multi-day scheduling), the platform bridges the gap between chaotic offline vendor coordination and modern e-commerce convenience.

---

## 2. Target User

### 2.1 Jobs To Be Done (JTBD)
- **Functional:** Browse standard and luxury event packages with transparent base pricing; customize specific requirements (catering, decor, DJ, photography, videography); submit bookings with venue and date details.
- **Emotional:** Feel relieved from vendor coordination stress and confident that cultural ceremonies (e.g., *Thirumanam*, *Seemantham*, *Kadhukuthu*, *Grahapravesam*) will be honored with professional dignity.
- **Social:** Showcase celebratory milestones to family, peers, and clients with top-tier aesthetic execution.
- **Contextual:** Plan events from mobile or desktop within Tamil Nadu with localized regional options (38 districts) and bilingual colloquial resonance.

### 2.2 Non-Users (v1)
- **Vendors/Subcontractors Seeking Self-Service Listing:** V1 uses in-house and partner fulfillment managed directly by Banana Brothers. Third-party vendor marketplace onboarding is out of scope.
- **Users Outside Tamil Nadu:** Logistics, district selectors, and pricing models are tailored specifically for Tamil Nadu operations.

### 2.3 Key User Journeys

- **UJ-1: First-Time Package Discovery and Custom Quote Submission**
  - **Persona + Context:** Karthik, planning his sister's wedding reception in Coimbatore.
  - **Entry State:** Unauthenticated visitor landing on the Home page via mobile browser.
  - **Path:** Clicks "Explore Packages" &rarr; views the 3 tier tiers on `Packages` &rarr; selects "Standard Classic Package" / "Royal Luxury Package" &rarr; enters event requirements, selects "Thirumanam", checks Photography, Catering, and DJ &rarr; sees live recalculated price estimate &rarr; fills in Coimbatore district, venue address, date/time span, and Google Maps pin &rarr; submits.
  - **Climax:** Receives immediate on-screen booking confirmation with estimate summary and reference code.
  - **Resolution:** Prompted to register/login to track booking progress in "My Events".
  - **Edge Case:** If Karthik selects a date span spanning 3 days, the system multiplies daily recurring base costs dynamically while maintaining flat decor setup fees.

- **UJ-2: Direct A La Carte Service Booking**
  - **Persona + Context:** Divya, organizing an intimate 1st birthday party in Chennai with a strict budget.
  - **Entry State:** Authenticated user searching specifically for birthday decorations.
  - **Path:** Navigates to `Services` &rarr; clicks "Birthdays" filter &rarr; selects "Birthday Parties" or "Stage Decorations" &rarr; reviews starting price &rarr; routes into the custom booking configurator.
  - **Climax:** Configures specific needs without being forced into a rigid all-inclusive wedding package.
  - **Resolution:** Booking recorded under her profile.

- **UJ-3: Customer Order Tracking via "My Events"**
  - **Persona + Context:** Anbu, who booked an engagement event scheduled for next month.
  - **Entry State:** Authenticated customer returning to check booking status.
  - **Path:** Clicks "My Events" on the navigation bar &rarr; views list of cards segmented by status (`Upcoming` vs `Completed`) &rarr; reviews event date, location, and package details.
  - **Climax:** Clear visual confirmation of event readiness without needing back-and-forth phone inquiries.

---

## 3. Glossary
- **Package Tier:** Pre-bundled event offerings categorized into **High** (*Royal Luxury*), **Medium** (*Standard Classic*), and **Low** (*Budget Friendly*).
- **Service (A La Carte):** Individual event capability that can be booked independently (e.g., Wedding Planners, Catering, Photography, DJ Music).
- **Add-On Need:** Modular service item selected within a package booking (e.g., Food, Catering, Decorations, Cosmetics, DJ Music, Photography, Videography, Lighting).
- **District Scope:** One of the 38 administrative districts of Tamil Nadu supported for venue assignment.
- **Estimated Base Amount:** Dynamic real-time calculation combining base package cost, selected add-ons, and event duration (number of days).
- **Event Status:** Operational lifecycle state of a booking (`Upcoming`, `In Progress`, `Completed`, `Cancelled`).

---

## 4. Features & Functional Requirements

### 4.1 Global Navigation & Header
**Description:** Persistent header across all pages providing brand identity, quick access to primary sections, real-time search, and direct account shortcuts. Realizes UJ-1, UJ-3.

#### FR-1: Primary Navigation Bar
The system shall display a responsive navigation bar containing the Banana Brothers brand logo, links to **Home**, **Services**, **Packages**, and **My Events**, an integrated search box, a **My Bookings** shortcut, and a **User Login/Profile** shortcut.
- **Consequences (testable):**
  - On desktop (&gt;850px), links remain centered with underline hover animations and brand logo left-aligned.
  - On mobile (&le;850px), the nav stacks into a compact two-row header with responsive search input.

#### FR-2: Search Capability
Users can type keywords into the search box to discover matching services or packages.
- **Consequences (testable):**
  - Entering "catering" or "wedding" filters or navigates to relevant service cards.
  - Submitting an empty query keeps the user on the current view without errors.

---

### 4.2 Hero Section & Brand Storytelling
**Description:** High-impact landing page hero communicating core value proposition, Tamil/English colloquial welcome, proof metrics, and primary CTAs. Realizes UJ-1.

#### FR-3: Hero Showcase & Action Triggers
The landing hero shall feature the tagline *"Crafting Unforgettable Experiences"*, bilingual narrative, trust badge (*"Top Rated / 500+ Events Done"*), and two primary call-to-action buttons: **Explore Packages** and **Book Event**.
- **Consequences (testable):**
  - Clicking "Explore Packages" routes directly to the Packages section.
  - Clicking "Book Event" opens the tier selection or custom booking workflow.

---

### 4.3 Service Catalog & Filtering
**Description:** Comprehensive showcase of 12 distinct event services with category pill filters and transparent starting price indicators. Realizes UJ-2.

#### FR-4: Service Categorization & Dynamic Filtering
The platform shall display 12 standardized services:
1. Wedding Planners (Starting from ₹1,50,000)
2. Reception & Engagement (Starting from ₹80,000)
3. Corporate Events (Starting from ₹75,000)
4. Cultural Events (Starting from ₹50,000)
5. Birthday Parties (Starting from ₹25,000)
6. Baby Shower (Starting from ₹35,000)
7. Surprise Events (Starting from ₹15,000)
8. Stage Decorations (Starting from ₹20,000)
9. Catering Services (Starting from ₹250 / plate)
10. Photography (Starting from ₹30,000)
11. Videography (Starting from ₹40,000)
12. Entertainment & DJ (Starting from ₹18,000)

- **Consequences (testable):**
  - Users can filter cards by **All Services**, **Weddings**, **Birthdays**, **Corporate**, and **Entertainment**.
  - Clicking filter pills immediately hides non-matching cards without page reload.
  - Each card provides a "Book Now" CTA initiating booking configuration for that service.

---

### 4.4 Tiered Package System
**Description:** Structured pricing packages catering to high-end luxury, mainstream classic, and budget-conscious events. Realizes UJ-1.

#### FR-5: Package Tier Specifications
The system shall present three primary tiers:
- **High Package (Royal Luxury Package):** Starting from ₹3,50,000 base. Grand stage decor, imported floral setups, 4K cinematic videography, drone coverage, lavish multi-course buffet catering.
- **Medium Package (Standard Classic Package):** Starting from ₹1,20,000 base (configurator baseline ₹75,000). Flower arc background, candid photography, sound & DJ setup, theme cake table, catering service.
- **Low Package (Budget Friendly Package):** Starting from ₹25,000 base (configurator baseline ₹30,000). Minimalist stage backdrop, balloon arches, focus LED lighting, basic audio.

- **Consequences (testable):**
  - Each package card displays high-resolution visual preview, tier badge, included feature highlights, starting price, and "Book Package" trigger.

---

### 4.5 Two-Step Booking & Live Estimator Configurator
**Description:** Interactive multi-step booking engine capturing customer contact, traditional function category, modular add-on needs, venue location across Tamil Nadu, date/time scheduling, and real-time total price calculation. Realizes UJ-1, UJ-2.

#### FR-6: Step 1 – Customer & Event Requirements
The system shall collect:
- Full Name (required)
- Mobile Number (10 digits, validated regex, required)
- Alternative Mobile Number (optional)
- Email Address (validated email format, required)
- Function Category (Dropdown covering: Wedding/Thirumanam, Reception, Birthday Party, Engagement/Ring Ceremony, Seemantham/Baby Shower, Ear Piercing/Kadhukuthu, Puberty Function/Manjal Neerattu Vizha, Housewarming/Grahapravesam, Anniversary Celebration, Corporate Gala & Conference)
- Modular Add-On Needs checkboxes with explicit pricing:
  - Food (+₹40,000)
  - Catering (+₹25,000)
  - Decorations (+₹35,000)
  - Cosmetics (+₹15,000)
  - DJ Music (+₹20,000)
  - Photography (+₹30,000)
  - Videography (+₹35,000)
  - Lighting (+₹15,000)

- **Consequences (testable):**
  - Toggling any checkbox immediately updates the live price summary box.
  - Form validation prevents advancing to Step 2 if mandatory fields are missing or improperly formatted.

#### FR-7: Step 2 – Venue, Geolocation & Schedule
Upon completing Step 1, Step 2 expands and collects:
- District Dropdown (covering all 38 Tamil Nadu districts: Ariyalur, Chengalpattu, Chennai, Coimbatore, Cuddalore, Dharmapuri, Dindigul, Erode, Kallakurichi, Kanchipuram, Kanyakumari, Karur, Krishnagiri, Madurai, Mayiladuthurai, Nagapattinam, Namakkal, Nilgiris, Perambalur, Pudukkottai, Ramanathapuram, Ranipet, Salem, Sivaganga, Tenkasi, Thanjavur, Theni, Thoothukudi, Tiruchirappalli, Tirunelveli, Tirupathur, Tiruppur, Tiruvallur, Tiruvannamalai, Tiruvarur, Vellore, Viluppuram, Virudhunagar).
- Place / Area (required text).
- Full Hall/Venue Address (required text).
- Pincode (6 digits, validated regex, required).
- From Date & To Date (date pickers, required).
- From Time & To Time (time pickers, required).
- Google Map Location Link (valid URL, required).

- **Consequences (testable):**
  - If `toDate` &gt; `fromDate`, the duration in days `diffDays = Math.ceil((end - start)/(1000*60*60*24)) + 1` multiplies the calculated base sum accordingly.
  - Submitting final order triggers order record creation, generates a unique booking ID, and presents a success confirmation summary.

---

### 4.6 Customer Portal: "My Events"
**Description:** Dedicated management dashboard for registered customers to track their booked events. Realizes UJ-3.

#### FR-8: Event Status Dashboard
The system shall display all bookings associated with the authenticated user with:
- Visual event cover photo.
- Status badge (`Upcoming` in white/black pill, `Completed` in solid black pill).
- Scheduled Event Date.
- Event Title and brief description.
- Venue Location (District / Hall name).
- "View Details" action button to inspect the full booking breakdown.

---

### 4.7 User Authentication & Security
**Description:** Account registration, OTP verification, credential login, and password recovery. Realizes UJ-1, UJ-3.

#### FR-9: Registration with Email OTP Verification
Users can register by supplying First Name, Last Name, Username, Email, OTP verification (6 digits), Age, and Password confirmation.
- **Consequences (testable):**
  - "Send OTP" simulates or dispatches a 6-digit one-time code to the supplied email.
  - Password and Confirm Password must match before submission is enabled.
  - Age must fall between 1 and 120.

#### FR-10: Login & Password Reset
- Registered users can log in using Email/Username and Password.
- "Forgot Password" flow allows entering registered email, requesting verification OTP, and submitting a new password.

---

### 4.8 Footer & Support Infrastructure
**Description:** Standardized site footer delivering contact information, service links, package links, social/legal links, and copyright notices.

#### FR-11: Footer Information Architecture
- Displays head office address (*Chennai, Tamil Nadu, India*), official contact email (`contact@bananabrothers.com`), and phone number (`+91 98765 43210`).
- Quick Links (Home, About Us, My Events, Bookings).
- Categorized Services and Packages links.
- Legal links (Privacy Policy, Terms of Use, FAQ).

---

## 5. Non-Goals (Explicit)
- **Direct Online Payment Gateway in v1:** Online checkout (Stripe/Razorpay card processing) is deferred to v1.1. In v1, order submission generates a formal booking quote request and reservation placeholder, followed by offline advance payment verification.
- **Multi-Vendor Marketplace:** The platform is exclusive to Banana Brothers operations; no external vendor self-registration portal.
- **Automated Venue Availability Engine:** Hall availability is not synchronized via calendar APIs; feasibility is confirmed manually by team dispatchers.
- **Multi-State / International Bookings:** Restricted to Tamil Nadu districts only.

---

## 6. MVP Scope

### 6.1 In Scope (v1)
- Complete responsive frontend website (Home, Services, Packages, My Events, Auth).
- 12 service catalog items with active filter tabs.
- 3 package tiers with dedicated detailed booking pages.
- 2-step booking modal/page with dynamic pricing calculation, Tamil Nadu 38-district selector, and date range calculation.
- Client-side and backend-ready user authentication flow with OTP verification simulation.
- Customer dashboard displaying Upcoming and Completed bookings.

### 6.2 Out of Scope for MVP (Deferred to v2)
- Automated SMS notifications via Twilio/Gupshup `[Deferred to v2]`.
- Direct payment gateway integration (Razorpay/UPI deep links) `[Deferred to v1.1]`.
- Customer reviews and ratings submission engine `[Deferred to v2]`.
- Admin dashboard for Banana Brothers staff to accept, assign, and reschedule orders `[Deferred to Sprint 2 / v1.2]`.

---

## 7. Success Metrics

### Primary
- **SM-1 (Booking Conversion Rate):** &ge; 12% of users who enter Step 1 of the booking configurator complete Step 2 and submit the order. Validates FR-6, FR-7.
- **SM-2 (Estimate Accuracy):** &le; 5% variation between the configurator's estimated base amount and the final operational quote issued to the customer. Validates FR-5, FR-6.

### Secondary
- **SM-3 (Account Creation Rate):** &ge; 40% of first-time bookers complete registration or login during or immediately after the booking flow. Validates FR-9, FR-10.
- **SM-4 (Mobile Usability Rate):** &ge; 95% error-free completion on mobile devices (&le;600px). Validates FR-1, FR-6, FR-7.

### Counter-Metrics (Do Not Optimize)
- **SM-C1 (Quote Spam Volume):** Do not maximize raw booking clicks if lead drop-off after contact is high. Maintain mandatory phone and email verification to filter out fake submissions.
- **SM-C2 (Add-On Overloading):** Do not maximize checkbox selections by aggressive bundling if it increases user cart abandonment in Step 1.

---

## 8. Open Questions
1. **Advance Deposit Requirement:** What percentage of advance payment (e.g., 25% or 50%) should be collected upon booking confirmation?
2. **Cancellation & Refund Policy:** What are the allowable cancellation windows prior to event execution (e.g., full refund &gt; 14 days, 50% &gt; 7 days)?
3. **Backend & Database Selection:** Should the persistence layer utilize SQLite / PostgreSQL with Node.js/Python, or a cloud backend like Supabase / Firebase?
4. **Live SMS/Email Delivery:** Which Indian SMS DLT provider or email SMTP service should be integrated for live transactional OTPs?

---

## 9. Assumptions Index
- `[ASSUMPTION: §4.4]` High, Medium, and Low packages serve as baseline packages starting at ₹3,50,000, ₹1,20,000, and ₹25,000 respectively, with custom configurator baselines calibrated to ₹1,50,000, ₹75,000, and ₹30,000.
- `[ASSUMPTION: §4.5]` Event duration of more than 1 day multiplies the base package total by the number of active days.
- `[ASSUMPTION: §4.7]` Registration OTP verification in MVP can operate via simulated client modal before connecting to an active DLT SMS gateway.
- `[ASSUMPTION: §5]` Booking submissions generate an internal review ticket for the Banana Brothers coordinator team to contact the customer within 24 hours.
