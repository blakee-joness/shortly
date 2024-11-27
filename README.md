# Shortly
A URL shortening service that converts long URLs into shorter, manageable links. It also provides analytics for the shortened URLs.

## Functional Requirements

### In Scope

- [ ] Allow users to submit a long URL and receive a shortened version.
    - [ ] Optionally, enable users to specify a custom alias for their shortened URL.
    - [ ] Optionally, enable users to set an expiration date for their shortened URL.
- [ ] Provide users with the ability to access the original URL using the shortened URL.

### Out of Scope

- Authentication
- Analytics on link clicks (example: click counts, geographic data).

## Non-functional Requirements

### In Scope

- [ ] Ensure uniqueness for short codes (no two long URLs should map to the same short URL).
- [ ] Redirection should occur with minimal delay (< 100ms).
- [ ] Ensure system reliability and availability of 99.99% (availability > consistency).
- [ ] Scale to support 1 billion shortened URLs and 100 million daily active users (DAU).

### Out of Scope

- Data consistency in real-time analytics.
- Advanced security features like spam detection and malicious URL filtering.

## High-Level Data Structure

### URL Model

This database table stores information about shortened URLs. Each row contains a unique identifier, the original URL, the shortened URL, and the user who created it.

| URL ID | Original URL               | Shortened URL | Creation   | Expiration | User ID |
|--------|----------------------------|---------------|------------|------------|---------|
| 1      | somereallylong.url/1234    | short.ly/aBc  | 2024-01-01 | 2025-01-01 | 4       |
| 2      | anotherreallylong.url/1234 | short.ly/deF  | 2024-02-02 | 2025-02-02 | 5       |

### API Response

To create a shortened URL, the payload would look like this:

**POST Request to `/shorten`**

```json
{
    "long_url": "somereallylong.url/1234",
    "custom_alias": "optional_custom_alias",
    "expiration_date": "optional_expiration_date"
}
```

**Response:**

```json
{
    "short_url": "http://short.ly/aBc"
}
```

### Accessing Shortend URLs
**GET Request to Access Shortened URL**

When a client browser makes a GET request to a shortened URL, the server will respond with a 302 status code, redirecting the client to the original URL.

Example:

**GET Request to `/short.ly/aBc`**

**Response:**

```
HTTP/1.1 302
Location: http://somereallylong.url/aBc
```
