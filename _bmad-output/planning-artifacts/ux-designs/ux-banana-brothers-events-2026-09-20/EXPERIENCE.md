---
name: Banana Brothers Events
status: draft
sources:
  - {planning_artifacts}/prds/prd-banana-brothers-events-2026-09-20/prd.md
updated: 2026-09-20
---

# Banana Brothers Events — Experience Specification

## 1. Foundation
Banana Brothers is a multi-page responsive web experience optimized for desktop browsers, tablets, and mobile devices across Tamil Nadu, India. 

The platform inherits its visual rules directly from [`DESIGN.md`](file:///c:/Users/91995/OneDrive/Documents/Event%20website/_bmad-output/planning-artifacts/ux-designs/ux-banana-brothers-events-2026-09-20/DESIGN.md). The user experience prioritizes **clarity, zero-friction discovery, cultural familiarity, and immediate feedback**.

- **Form Factor**: Responsive Web (Mobile-First responsive breakpoints: `320px`, `550px`, `650px`, `768px`, `850px`, `992px`, `1050px`).
- **Design System**: Monochromatic vanilla HTML5 / CSS3 architecture grounded in the existing prototype files (`_bmad/New Pro`).
- **Surface Language**: High-contrast light surfaces (`#ffffff`) with tactile blueprint background (`bg_blue.png`) and solid black ink (`#111111`).

---

## 2. Information Architecture (IA)

| Surface | File Reference | Reached From | Purpose & Primary Actions |
|---|---|---|---|
| **Home** | `Home.html` | Root `/`, Navbar `Home`, Brand Logo | Brand introduction, trust stats (`500+ Events Done`), primary CTAs (`Explore Packages`, `Book Event`). |
| **Global Navbar** | `Navbar.html` | Persistent across all pages | Global navigation, keyword search, shortcut to My Bookings, shortcut to User Login. |
| **Services Catalog** | `Services.html` | Navbar `Services`, Footer links | 12 A la carte event services with interactive category pills (`All`, `Weddings`, `Birthdays`, `Corporate`, `Entertainment`). |
| **Packages Showcase** | `Pakages.html` | Navbar `Packages`, Home Hero CTA, Footer | 3 Tier cards (`High`, `Medium`, `Low`) with starting prices and `Book Package` triggers. |
| **High Tier Configurator** | `High.html` | `Pakages.html` ("Royal Luxury"), Direct link | 2-step booking engine for high-end luxury events (base ₹1,50,000 + add-ons * days). |
| **Medium Tier Configurator** | `Mediam.html` | `Pakages.html` ("Standard Classic"), Direct link | 2-step booking engine for classic mid-tier events (base ₹75,000 + add-ons * days). |
| **Low Tier Configurator** | `Low.html` | `Pakages.html` ("Budget Friendly"), Direct link | 2-step booking engine for budget events (base ₹30,000 + add-ons * days). |
| **My Events** | `Myevents.html` | Navbar `My Events`, Icon `My Booking`, Footer | Customer dashboard listing active and past bookings with `Upcoming` and `Completed` status pills. |
| **Login** | `Login.html` | Navbar `User Login` icon, Register redirect | Email/Username and password login, link to Register and Forgot Password. |
| **Register** | `Register.html` | Login page redirect | Account registration with live inline Email OTP verification and password confirmation. |
| **Forgot Password** | `Forget.html` | Login page redirect | Password recovery with email OTP verification and new password reset. |
| **Footer** | `Footer.html` | Persistent across all pages | Office contact information (Chennai, TN), quick links, services directory, support links, legal terms. |

---

## 3. Voice and Tone (Microcopy)

The platform speaks with **authoritative elegance paired with warm, colloquial Tamil resonance**.

| Surface / Context | Do (Existing Pattern) | Don't |
|---|---|---|
| **Landing Hero Subtitle** | *"Ungaludaiya special moments-a mass-ana memory-a maatha naanga ready! Premium event management, custom packages, and seamless booking—ellame ore idathula."* | Generic English corporate boilerplate without personality. |
| **Pricing Labels** | *"Starting from"* (Small, 0.68rem uppercase) + *"₹3,50,000"* | Obscure fees or hidden quotes. |
| **Category Selection** | Traditional Tamil nomenclature in parentheses: *"Wedding (Thirumanam)"*, *"Ear Piercing (Kadhukuthu)"*, *"Housewarming (Grahapravesam)"*. | Purely Western event categories that disconnect from local celebrations. |
| **Validation Toast** | *"OTP sent to your email!"*, *"OTP verified successfully!"*, *"Registration details submitted!"* | Generic alert boxes or cold error codes. |
| **Order Success** | *"Your [Tier] Package Order has been placed successfully! Estimated Amount: ₹ X"* | Ambiguous confirmation without price summary. |

---

## 4. Component Patterns & Behaviors

### 4.1 Global Navigation Bar
- **Logo Click**: Returns to Home surface.
- **Nav Link Hover**: Triggers a progressive left-to-right underline animation (`transform: scaleX(1)` from `origin: left`).
- **Search Bar**: Fixed width `280px` (desktop), collapses to `85px` on mobile screens. Dispatches query on Enter or button click.
- **Quick Icon Actions**: Square buttons (`34px`) that invert from white to solid black on hover.

### 4.2 Dynamic Filter Pills (`Services.html`)
- Displays 5 pills: `All Services`, `Weddings`, `Birthdays`, `Corporate`, `Entertainment`.
- **Default State**: `All Services` has `.filter-btn.active` (solid black background, white text).
- **Interaction**: Clicking any pill switches the `.active` class to the clicked pill, showing only corresponding services.

### 4.3 Two-Step Interactive Booking Engine (`High.html`, `Mediam.html`, `Low.html`)
- **Visual Anchor**: Continuous 3-image sliding gallery at top (`150px` height) providing immediate visual context.
- **Step 1 — Contact & Scope Configuration**:
  - Full Name, 10-digit Mobile, Alternative Mobile, Email Address.
  - Function Category Dropdown (10 options).
  - 8 Checkbox cards representing modular needs (*Food, Catering, Decorations, Cosmetics, DJ Music, Photography, Videography, Lighting*).
  - **Live Dynamic Price Engine**: Selecting any checkbox instantly adds its discrete amount to the package base and updates the large `#totalPriceDisplay`.
  - **Advance Trigger**: Submitting Step 1 validates required fields, then unlocks Step 2.
- **Step 2 — Venue Geolocation & Multi-Day Schedule**:
  - Unrolls below Step 1 with `animation: fadeIn 0.4s ease` and smoothly scrolls into view (`scrollIntoView({ behavior: 'smooth' })`).
  - Pre-populated dropdown of all 38 Tamil Nadu districts.
  - Place/Area, Full Venue/Hall Address, 6-digit Pincode.
  - From/To Date & From/To Time pickers.
  - **Duration Multiplier**: When `diffDays > 1`, `calculateTotal()` dynamically calculates `total = total * diffDays`.
  - Google Map URL input ensuring delivery crew can pinpoint the venue.
  - **Final Order Submission**: Displays confirmation alert summarizing total estimated price.

### 4.4 Inline Verification Inputs (`Register.html`, `Forget.html`)
- Combined input with inline button (`.input-with-action`):
  - Email field with attached `Send OTP` button.
  - OTP field with attached `Verify` button.
- Triggers non-intrusive floating toast message (`.msg-box`) positioned top-center for `2500ms`.

---

## 5. State Patterns

| State | Surface | Manifestation / Behavior |
|---|---|---|
| **Default / Initial** | Booking Configurator | Step 1 active; Step 2 container hidden (`display: none`). Live price reflects package base price. |
| **Step 2 Revealed** | Booking Configurator | Step 2 container appended with `.active` class (`display: block; animation: fadeIn`). |
| **Add-On Selected** | Booking Step 1 | Checkbox accent color turns black; live base price increments immediately. |
| **Multi-Day Range** | Booking Step 2 | Changing `toDate` to later date immediately multiplies base sum and updates display. |
| **Notification Toast** | Auth Screens | `.msg-box` appears with `display: block` at `top: 20px`, auto-dismisses after 2.5s. |
| **Event Status Tag** | My Events | `.status-upcoming` (white with black border) or `.status-completed` (solid black pill). |

---

## 6. Interaction Primitives

- **Click to Navigate**: Direct anchors for top navigation links and footer columns.
- **Step Progression**: Form submission with client validation (`required`, regex patterns `[0-9]{10}`, `[0-9]{6}`) before exposing Step 2.
- **Smooth Scroll**: Automatic programmatic scroll to newly expanded form sections.
- **Real-Time Input Listening**: `onchange="calculateTotal()"` bound to all add-on checkboxes and date inputs.
- **CSS Keyframe Automation**: Ambient 12s infinite sliding carousel for package highlights.

---

## 7. Accessibility Floor

- **Form Labels**: Every input, select, and textarea is explicitly paired with a `<label>` element specifying `for="fieldId"`.
- **Keyboard Navigation**: Form tab order flows logically from personal details &rarr; function type &rarr; add-ons &rarr; venue details &rarr; date ranges.
- **High Contrast Assurance**: 
  - Primary text (`#111111`) on pure white background (`#ffffff`) delivers a contrast ratio of `17.4:1`, well exceeding WCAG AAA standards.
  - Inverted buttons (`#ffffff` text on `#000000` / `#111111`) deliver maximum readability.
- **Touch Targets**: Mobile buttons (`.book-btn`, `.filter-btn`, `.icon-btn`, `.btn-primary`) are sized for comfortable thumb interaction with generous touch targets.
- **Visual Feedback**: Inputs provide clear focus states with solid black outlines (`#000000`).

---

## 8. Key User Flows

### Flow 1: High Package Configuration & Order Submission
*Protagonist: Vignesh, booking a luxury wedding reception in Madurai.*

1. **Discovery**: Vignesh arrives on `Home.html`, reads the bilingual welcome, and clicks **Explore Packages**.
2. **Evaluation**: Navigates to `Pakages.html`. Reviews the three tiers; selects **Royal Luxury Package** (`₹3,50,000`). Clicks **Book Package**.
3. **Configuration (Step 1)**: Routes to `High.html`.
   - Ambient gallery scrolls top decor photos.
   - Enters Full Name, Mobile, Email.
   - Selects Function Category: `Reception`.
   - Selects Add-on Checkboxes: `Food` (+₹40,000), `Videography` (+₹35,000), `DJ Music` (+₹20,000).
   - Observes price summary automatically increment to `₹ 2,45,000`.
   - Clicks **Next Step &rarr;**.
4. **Venue & Schedule (Step 2)**:
   - Form expands smoothly with fade animation.
   - Selects District: `Madurai`.
   - Enters Area: `KK Nagar`.
   - Enters Venue Address: `Meenakshi Kalyana Mandapam, 4th Main Road`.
   - Enters Pincode: `625020`.
   - Selects From Date and To Date (2 days duration).
   - The price display recalculates to reflect the multi-day factor.
   - Pastes Google Maps link.
5. **Climax & Confirmation**: Vignesh clicks **BOOK YOUR ORDER NOW**. An order confirmation dialog appears with his order summary and estimated pricing.

---

### Flow 2: Quick Service Lookup & Booking
*Protagonist: Selvi, organizing a birthday celebration in Chennai.*

1. **Discovery**: Selvi clicks **Services** on the top navigation bar (`Services.html`).
2. **Filtering**: Clicks the **Birthdays** category filter pill. The grid instantly filters to show "Birthday Parties" and related setup options.
3. **Inspection**: Reviews the card details: *"Customized themed birthday setups for children and adults with fun activities and decorative cake tables. Starting from ₹25,000"*.
4. **Action**: Clicks **Book Now** to initiate booking and date reservation.

---

### Flow 3: Checking Event Milestones
*Protagonist: Ramesh, tracking an upcoming anniversary event.*

1. **Navigation**: Ramesh clicks **My Events** (or clicks the calendar icon button on the navbar).
2. **Dashboard**: Views `Myevents.html`.
3. **Status Review**: Observes his card marked with the white/black **UPCOMING** badge, noting date, venue, and description.
4. **Details Inspection**: Clicks **View Details** to review the full equipment checklist and booking details.
