---
name: Banana Brothers Events
description: Premium, minimalist, monochromatic event management and booking platform for Tamil Nadu.
colors:
  bg-canvas: '#ffffff'
  bg-pattern: 'url(bg_blue.png)'
  surface-primary: '#ffffff'
  surface-secondary: '#fafafa'
  surface-muted: '#f4f4f4'
  surface-pill: '#f2f2f2'
  text-primary: '#111111'
  text-heading: '#222222'
  text-body: '#333333'
  text-muted: '#555555'
  text-subtle: '#666666'
  text-placeholder: '#999999'
  border-dark: '#111111'
  border-medium: '#e0e0e0'
  border-light: '#eeeeee'
  border-subtle: '#f0f0f0'
  tier-high-bg: '#111111'
  tier-high-text: '#ffffff'
  tier-medium-bg: '#555555'
  tier-medium-text: '#ffffff'
  tier-low-bg: '#ffffff'
  tier-low-text: '#111111'
  tier-low-border: '#111111'
  status-completed-bg: '#111111'
  status-completed-text: '#ffffff'
  status-upcoming-bg: '#ffffff'
  status-upcoming-text: '#111111'
  status-upcoming-border: '#111111'
typography:
  font-primary:
    fontFamily: "'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Oxygen, Ubuntu, Cantarell, sans-serif"
  font-serif:
    fontFamily: "'Georgia', 'Times New Roman', serif"
  hero-title:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '2.8rem'
    fontWeight: '800'
    lineHeight: '1.15'
    letterSpacing: '-0.8px'
  section-title:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '1.8rem'
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: '-0.4px'
  auth-title:
    fontFamily: "{typography.font-serif.fontFamily}"
    fontSize: '1.45rem'
    fontWeight: '400'
    lineHeight: '1.3'
  card-title:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '0.95rem'
    fontWeight: '700'
    lineHeight: '1.3'
  card-title-lg:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '1.15rem'
    fontWeight: '700'
    lineHeight: '1.3'
  body:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '0.85rem'
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '0.78rem'
    fontWeight: '400'
    lineHeight: '1.4'
  label:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '0.78rem'
    fontWeight: '600'
    lineHeight: '1.2'
  badge:
    fontFamily: "{typography.font-primary.fontFamily}"
    fontSize: '0.68rem'
    fontWeight: '700'
    letterSpacing: '1px'
    textTransform: 'uppercase'
rounded:
  none: '0px'
  xs: '2px'
  sm: '4px'
  md: '6px'
  lg: '10px'
  xl: '20px'
  full: '9999px'
spacing:
  gutter-desktop: '16px'
  gutter-mobile: '12px'
  container-auth: '310px'
  container-booking: '900px'
  container-catalog: '1050px'
  container-footer: '1100px'
  gap-sm: '8px'
  gap-md: '14px'
  gap-lg: '24px'
components:
  btn-primary:
    backgroundColor: "{colors.text-primary}"
    color: '#ffffff'
    borderRadius: "{rounded.md}"
    padding: '12px 26px'
    fontWeight: '600'
    fontSize: '0.92rem'
  btn-primary-compact:
    backgroundColor: "{colors.text-primary}"
    color: '#ffffff'
    borderRadius: "{rounded.xs}"
    padding: '8px 18px'
    fontWeight: '600'
    fontSize: '0.78rem'
  btn-secondary:
    backgroundColor: '#ffffff'
    color: "{colors.text-primary}"
    border: '1px solid #111111'
    borderRadius: "{rounded.md}"
    padding: '12px 24px'
    fontWeight: '600'
    fontSize: '0.92rem'
  filter-btn:
    backgroundColor: '#ffffff'
    color: "{colors.text-primary}"
    border: '1px solid #111111'
    borderRadius: "{rounded.xl}"
    padding: '6px 16px'
    fontSize: '0.78rem'
    fontWeight: '600'
  filter-btn-active:
    backgroundColor: "{colors.text-primary}"
    color: '#ffffff'
  input-field:
    backgroundColor: '#ffffff'
    border: '1px solid #e0e0e0'
    borderRadius: "{rounded.none}"
    padding: '10px 12px'
    fontSize: '0.85rem'
    color: "{colors.text-body}"
  input-field-auth:
    backgroundColor: '#ffffff'
    border: '1px solid #111111'
    borderRadius: "{rounded.none}"
    padding: '7px 9px'
    fontSize: '0.8rem'
    color: "{colors.text-body}"
---

# Banana Brothers Events — Visual Design Specification

## 1. Brand & Style
The aesthetic posture of **Banana Brothers Events** is defined by **monochromatic editorial precision, architectural restraint, and cultural groundedness**. 

Rather than relying on noisy festive colors, the design adopts a stark, high-contrast palette of pitch blacks (`#000000`, `#111111`), surgical off-whites, neutral boundary lines, and a subtle blueprint texture overlay (`bg_blue.png`). This creates a gallery-grade visual foundation where event photography (grand wedding stages, floral arches, banquet layouts) commands total visual hierarchy.

The typography balances clean technical modernism (`Segoe UI` system stack) with classical editorial warmth (`Georgia` serif headings for user authentication and milestone moments). Interfaces feel crisp, intentional, and executive-level.

---

## 2. Colors

### Core Canvas & Neutral Palette
- **`{colors.bg-canvas}` (`#ffffff`)**: The baseline luminous white page surface.
- **`{colors.bg-pattern}` (`url(bg_blue.png)`)**: Subtle textural depth applied consistently across the `body`, navbar, and footer.
- **`{colors.surface-primary}` (`#ffffff`)**: High-contrast card backgrounds, input backdrops, and active toggle surfaces.
- **`{colors.surface-secondary}` (`#fafafa`)**: Dedicated tone for calculation and summary breakdown panels.
- **`{colors.surface-pill}` (`#f2f2f2`)**: Neutral background for category badges and section tags.

### Typography & Ink Levels
- **`{colors.text-primary}` (`#111111`)**: Primary high-emphasis copy, navigation links, and primary CTA triggers.
- **`{colors.text-heading}` (`#222222`)**: Serif page titles and secondary headers.
- **`{colors.text-body}` (`#333333`)**: Standard body copy, form labels, and interactive values.
- **`{colors.text-muted}` (`#555555`)**: Secondary narrative text, contact info, and helper details.
- **`{colors.text-subtle}` (`#666666`)**: Subtitles, descriptions, and passive metadata.
- **`{colors.text-placeholder}` (`#999999`)**: Input field placeholders and inactive guides.

### Boundaries & Hairlines
- **`{colors.border-dark}` (`#111111`)**: High-contrast hairline borders for active buttons, dark badges, and auth input outlines.
- **`{colors.border-medium}` (`#e0e0e0`)**: Card container boundaries, navbar dividers, and booking input borders.
- **`{colors.border-light}` (`#eeeeee`)**: Checkbox cards, secondary dividers, and header underlines.
- **`{colors.border-subtle}` (`#f0f0f0`)**: Subtle internal card footers, image boundaries, and copyright dividers.

### Semantic Tier Badges
- **High Tier**: `{colors.tier-high-bg}` (`#111111`) with `{colors.tier-high-text}` (`#ffffff`). Solid black badge denoting supreme luxury.
- **Medium Tier**: `{colors.tier-medium-bg}` (`#555555`) with `{colors.tier-medium-text}` (`#ffffff`). Mid-gray badge denoting balanced standard classic.
- **Low Tier**: `{colors.tier-low-bg}` (`#ffffff`) with `{colors.tier-low-text}` (`#111111`) and `{colors.tier-low-border}` (`1px solid #111111`). Inverted white badge denoting budget-friendly accessibility.

---

## 3. Typography

### Typefaces
- **Primary Interface Font**: `'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`. Used for all UI controls, navigation, catalog cards, forms, tables, and buttons.
- **Editorial Serif Font**: `'Georgia', 'Times New Roman', serif`. Reserved exclusively for focused identity surfaces: Login, Register, and Forgot Password titles.

### Type Scale & Hierarchy
| Token | Font Family | Size | Weight | Line Height | Letter Spacing | Usage |
|---|---|---|---|---|---|---|
| `hero-title` | Primary | `2.8rem` (44.8px) | 800 | 1.15 | -0.8px | Hero header on landing page |
| `section-title` | Primary | `1.8rem` (28.8px) | 800 | 1.20 | -0.4px | Section main titles (`Services`, `Packages`, `My Events`, `Booking`) |
| `auth-title` | Serif | `1.45rem` - `1.6rem` | 400 | 1.30 | Normal | Dedicated auth modal headers |
| `card-title-lg`| Primary | `1.15rem` (18.4px) | 700 | 1.30 | Normal | Package titles, booking step headers |
| `card-title` | Primary | `0.95rem` (15.2px) | 700 | 1.30 | Normal | Service cards, My Events card titles |
| `body` | Primary | `0.85rem` (13.6px) | 400 | 1.50 | Normal | Subtitles, inputs, pricing values |
| `body-sm` | Primary | `0.78rem` (12.5px) | 400 | 1.40 | Normal | Card descriptions, venue labels |
| `label` | Primary | `0.78rem` (12.5px) | 600 | 1.20 | Normal | Form labels, navigation links (`0.98rem`) |
| `badge` | Primary | `0.68rem` (10.8px) | 700 | 1.00 | 1.0px | Pill badges, tier tags, status tags |

---

## 4. Layout & Spacing

### Max Width Containers
- **Catalog Container (`{spacing.container-catalog}`)**: `1050px` centered for `Services.html`, `Pakages.html`, and `Myevents.html`.
- **Booking Container (`{spacing.container-booking}`)**: `900px` centered for `High.html`, `Mediam.html`, and `Low.html`.
- **Footer Container (`{spacing.container-footer}`)**: `1100px` centered for site-wide footer.
- **Auth Container (`{spacing.container-auth}`)**: `290px` to `310px` centered for `Login.html`, `Register.html`, and `Forget.html`.

### Grids & Responsive Breakpoints
- **Desktop Grid (>850px)**:
  - Services: `grid-template-columns: repeat(3, 1fr)` with `18px` gap.
  - My Events: `grid-template-columns: repeat(3, 1fr)` with `18px` gap.
  - Booking Step 1 Form: `grid-template-columns: repeat(2, 1fr)` with `14px` gap.
  - Booking Add-On Services: `grid-template-columns: repeat(4, 1fr)` with `10px` gap.
- **Tablet Breakpoint (850px - 651px)**:
  - Navbar collapses to two-tier row (`logo` + `nav-right` top; `nav-links` bottom row centered).
  - Services grid transitions to `repeat(2, 1fr)`.
- **Mobile Breakpoint (<=650px / 550px)**:
  - Booking form collapses to `grid-template-columns: 1fr` (`full-width`).
  - Booking Add-On Services collapse to `repeat(2, 1fr)`.
  - Services grid collapses to `1fr` single-column stack at `550px`.
  - Packages cards convert to vertical flow with full-width action bar.

---

## 5. Elevation & Depth
Banana Brothers employs a **flat-graphic with tactile micro-depth** philosophy:
- **Default Surface**: Flat `1px solid #e0e0e0` / `#eeeeee` borders without drop shadows.
- **Interactive Card Hover**:
  - `transform: translateY(-3px)`
  - `box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06)`
  - `border-color: #111111`
- **Hero Floating Badge**:
  - `background: rgba(255, 255, 255, 0.92)`
  - `backdrop-filter: blur(8px)`
  - `box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1)`
- **Hero Image Container**:
  - `box-shadow: 0 15px 35px rgba(0, 0, 0, 0.07)`
  - Inner dark gradient overlay: `linear-gradient(135deg, rgba(0,0,0,0.25) 0%, rgba(0,0,0,0.75) 100%)`.

---

## 6. Shapes & Border Radii
- **Sharp / Architectural (`{rounded.none}` / `0px`)**: Form inputs (`.input-field`), navbar square icon buttons (`.icon-btn`).
- **Subtle Micro-Curve (`{rounded.xs}` / `2px`)**: Action buttons (`.book-btn`, `.view-btn`), tier badges (`.tier-badge`), status tags (`.status-tag`).
- **Card Framing (`{rounded.md}` / `6px`)**: Service cards, package cards, event cards, hero buttons (`.btn-primary`, `.btn-secondary`).
- **Floating Badges (`{rounded.lg}` / `10px`)**: Hero floating highlight card.
- **Pills & Badges (`{rounded.xl}` / `20px` & `{rounded.full}` / `50px`)**: Section pill badges (`.badge`), category filter buttons (`.filter-btn`).

---

## 7. Components

### 7.1 Navigation Bar (`Navbar.html`)
- **Container**: `width: 100%`, background `url(bg_blue.png)` over `#ffffff`, padding `12px 0`.
- **Brand**: Left-aligned logo (`bb.jpeg`), width `110px` (`85px` on mobile).
- **Links**: Centered flex list with `gap: 28px`. Color `#333333`, font size `0.98rem`, weight `600`.
  - **Hover Micro-interaction**: Left-to-right hairline underline animation (`after` pseudo-element, `height: 0.5px`, `transform-origin: left`, expanding via `scaleX(1)` in `0.3s`).
- **Search Box**: Right-aligned `280px` width box with `1px solid #e0e0e0`, transparent input, and search SVG icon.
- **Action Icons**: Square `34x34px` icon buttons (`My Booking` calendar icon, `User Login` avatar icon). On hover: solid `#000000` fill with `#ffffff` icon color.

### 7.2 Catalog Cards (`Services.html`, `Pakages.html`, `Myevents.html`)
- **Structure**: Image banner (`150px` - `260px` height, `object-fit: cover`) + Card Body with title, description, and footer.
- **Price Display**: Small uppercase label (`Starting from`, font size `0.68rem`) stacked above bold price value (`font-size: 0.88rem` - `1.05rem`, weight `800`).
- **Action Triggers**: Compact black buttons (`.book-btn`) with hover shift to `#333333`.

### 7.3 Two-Step Booking Form Engine (`High.html`, `Mediam.html`, `Low.html`)
- **Gallery Banner**: Full-width `150px` height slider track cycling 3 images in a `12s` CSS keyframe loop.
- **Form Card**: Flat white container with bordered inputs (`1px solid #e0e0e0`) and 2-column layout.
- **Checkbox Needs Card**: Individual `1px solid #eeeeee` card with accent black checkbox and service label.
- **Real-Time Price Box**: Dashed `#e0e0e0` box with background `#fafafa`, displaying estimated base amount in large bold font (`1.3rem`, weight `800`).
- **Step 2 Container**: Hidden by default, dynamically activates with `display: block`, `animation: fadeIn 0.4s ease`, and smooth scroll into view upon completing Step 1.

### 7.4 Auth Cards (`Login.html`, `Register.html`, `Forget.html`)
- **Container**: Centered vertical card (`max-width: 310px`), pure white with subtle background pattern.
- **Inputs**: Compact `7px 9px` fields with `1px solid #111111` border, focusing to solid black outline.
- **Inline Action Buttons**: Seamlessly integrated "Send OTP" and "Verify" buttons attached to email and OTP fields.
- **Feedback Toast (`.msg-box`)**: Centered fixed black pill (`#111111`, `#ffffff` text, font size `0.75rem`) auto-dismissing after `2500ms`.

---

## 8. Do's and Don'ts

### Do's
- **DO** preserve the exact layout and CSS values defined in the existing HTML files.
- **DO** maintain the high-contrast monochromatic color palette (`#111111` on `#ffffff`).
- **DO** use the left-to-right underline hover animation for all top-level navigation links.
- **DO** keep the exact 38 Tamil Nadu districts list in all booking venue dropdowns.
- **DO** retain the 2-step booking workflow with live JavaScript price calculation.

### Don'ts
- **DON'T** introduce arbitrary third-party color palettes (e.g., saturated blues, greens, or purples).
- **DON'T** alter existing form field IDs, placeholder texts, or button labels.
- **DON'T** replace the native CSS keyframe slider or responsive flex/grid layouts with heavy external UI frameworks.
- **DON'T** modify the existing HTML files; treat them as the immutable design source of truth.
