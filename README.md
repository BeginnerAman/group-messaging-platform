# GroupChat

A real-time group messaging platform built with Firebase Realtime Database and modern web technologies.

## Features

### Core Features
- Real-time Messaging: Send and receive messages instantly.
- Active Presence Tracking: View online status of participants.
- Typing Indicators: Visual notifications when users are composing messages.
- Message Threading: Quote and reply directly to specific messages.
- Message Reactions: Express feedback with emoji reactions.
- Edit and Delete: Update or remove messages with immediate database sync.
- Integrated Emoji Picker: Quick access to an extensive set of characters.

### Admin Controls
- Global Chat Mute: Disable messaging for all non-administrative users.
- Individual Participant Mute: Temporarily silence specific users.
- Clear History: Purge all messages from the database.
- Announcement System: Broadcast important notifications to all participants.
- Pinned Messages: Highlight key messages at the top of the interface.
- Rich Visual Effects: Broadcast animation triggers such as confetti or hearts.
- Message Highlighting: Emphasize admin messages with custom styling.

### UI and Accessibility Upgrades
- Clean Layout: Compact messaging spacing and premium dark mode.
- Iconography: Standard SVG icons replacing emoji UI controls.
- Keyboard Navigation: Close modals via the Escape key and focus visible styling.
- Responsive Design: Custom viewport scaling optimized for mobile devices.
- Accessibility Standards: Dynamic ARIA live status indicators, semantic markup, and WCAG AA contrast colors.

## Tech Stack
- Frontend: HTML5, CSS3, JavaScript (ES6)
- Database: Firebase Realtime Database

## Setup and Deployment

### 1. Configure Firebase
Update the `firebaseConfig` object in `app.js` with your Firebase project credentials:
```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  databaseURL: "YOUR_DATABASE_URL",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};
```

### 2. Launch Locally
No build process is required. Serve the files locally using any static web server:
```bash
# Example using python
python -m http.server 8000
```
Or open `index.html` directly in any web browser.

### 3. Deploy
The project consists of static files and can be hosted on GitHub Pages, Vercel, Netlify, or Firebase Hosting.
