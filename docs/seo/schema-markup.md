# Schema Markup Implementation

Use schema to help search engines interpret mortgage services, local presence, and trust content. Place JSON-LD in page templates or CMS modules where content is controlled and versioned.

## Organization
### Use Case
Represents the business brand entity across the site.

### Where It Belongs
Global template (home page and/or site-wide organizational reference).

### JSON-LD Starter Example
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Mortgage Group",
  "url": "https://www.example.com",
  "logo": "https://www.example.com/assets/logo.png",
  "sameAs": [
    "https://www.linkedin.com/company/example-mortgage-group",
    "https://www.facebook.com/examplemortgagegroup"
  ]
}
```

### Implementation Notes
- Keep business name and URL consistent with on-page content.
- Update `sameAs` profiles when social URLs change.

## LocalBusiness
### Use Case
Defines local business identity, address, and contact details.

### Where It Belongs
Contact page, key location pages, and business profile pages.

### JSON-LD Starter Example
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Example Mortgage Group",
  "telephone": "+1-512-555-0101",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "100 Market St",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78701"
  },
  "areaServed": ["Austin", "Round Rock", "Cedar Park"]
}
```

### Implementation Notes
- Keep NAP aligned with Google Business Profile and citations.
- Only include service areas that are operationally valid.

## MortgageBroker
### Use Case
Clarifies mortgage brokerage service offering.

### Where It Belongs
Primary service pages and about/service overview pages.

### JSON-LD Starter Example
```json
{
  "@context": "https://schema.org",
  "@type": "MortgageBroker",
  "name": "Example Mortgage Group",
  "url": "https://www.example.com/mortgage-services",
  "areaServed": "Texas",
  "telephone": "+1-512-555-0101"
}
```

### Implementation Notes
- Pair with clear service descriptions on-page.
- Avoid adding unsupported claims in structured fields.

## FAQPage
### Use Case
Supports common mortgage questions on FAQ-style sections.

### Where It Belongs
FAQ pages and service pages with visible FAQ blocks.

### JSON-LD Starter Example
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How quickly can I get pre-approved?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most borrowers receive initial pre-approval guidance within one business day."
      }
    }
  ]
}
```

### Implementation Notes
- FAQ content in JSON-LD must match visible content.
- Keep answers accurate and compliance-reviewed.

## Review
### Use Case
Represents customer feedback and trust signals.

### Where It Belongs
Testimonials/reviews sections where reviews are genuinely displayed.

### JSON-LD Starter Example
```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "author": {
    "@type": "Person",
    "name": "Verified Borrower"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "5",
    "bestRating": "5"
  },
  "reviewBody": "The team made our refinance process clear and fast."
}
```

### Implementation Notes
- Use only authentic, permissioned review content.
- Keep review display and structured data in sync.

## BreadcrumbList
### Use Case
Helps search engines understand page hierarchy and navigation.

### Where It Belongs
Templates with breadcrumb navigation (service, location, blog, FAQ pages).

### JSON-LD Starter Example
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.example.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Mortgage Services",
      "item": "https://www.example.com/mortgage-services"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Pre-Approval",
      "item": "https://www.example.com/pre-approval"
    }
  ]
}
```

### Implementation Notes
- Ensure breadcrumb URLs match canonical URLs.
- Keep breadcrumb order consistent with visible navigation.

## Validation And Monitoring
- Validate markup with Schema Markup Validator and Rich Results Test.
- Re-test after template changes, CMS migrations, or plugin updates.
- Monitor Google Search Console for enhancement warnings and drops in eligible rich results.
