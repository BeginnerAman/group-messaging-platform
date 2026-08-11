<p align="center">
  <img src="./icons/icon-192.png" alt="GroupChat Logo" width="128" height="128">
</p>

<h1 align="center">GroupChat</h1>

<p align="center">
  A premium, high-performance real-time group messaging platform optimized as an installable Progressive Web App (PWA). Powered by Firebase Realtime Database and built entirely with vanilla web technologies.
</p>

<p align="center">
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS"><img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"></a>
  <a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firebase"></a>
  <a href="https://web.dev/progressive-web-apps/"><img src="https://img.shields.io/badge/PWA-5A0FC8?style=for-the-badge&logo=progressive-web-app&logoColor=white" alt="PWA"></a>
</p>

---

## Key Features

### Messaging Experience
- **Real-time Synchronization**: Messages sync instantly across all clients using Firebase Realtime Database event listeners.
- **Message Threading**: Users can reply to specific messages, creating a clean conversational hierarchy with jump-to-quote navigation.
- **Rich Message Actions**: Supports inline edit, delete, and quick reactions for all chat participants.
- **Active Presence Tracking**: Displays real-time online status indicators and interactive typing notifications.
- **Integrated Emoji Keyboard**: Quick access to a comprehensive catalog of emojis directly from the message panel.

### Administrative Capabilities
- **Hashed Security Configuration**: System administrators configure passwords securely hashed with SHA-256 using the native Web Crypto API.
- **Global Control**: Toggle global chat muting or clear the database history with a single action.
- **Targeted Muting**: Temporarily silence specific users directly from the online users roster.
- **Announcement Toast**: Broadcast notifications to all users with dedicated visual alerts.
- **Pinned Messages**: Pin critical messages to the top header for persistent visibility.
- **Birthday Wishing Cards**: Send highly customized birthday wishes featuring special golden-gradient cards.
- **Celebration Effects**: Trigger a falling rain of colorful SVG cakes, gifts, balloons, and stars across the screen.

### PWA and UX Enhancements
- **Installable Desktop/Mobile App**: Standard PWA manifest files allow the platform to be added directly to the home screen or dock.
- **Offline Reliability**: Service Worker integration enables rapid page loads by caching essential assets.
- **Responsive Layout**: Designed from the ground up for seamless compatibility across iOS, Android, tablet, and desktop screens.
- **Universal Share Utility**: Integrated with the native Web Share API to easily invite friends or copy chat links.
- **Accessibility (WCAG AA)**: High-contrast color choices, semantic HTML elements, ARIA live-logs, and full keyboard accessibility.

---

## Technical Stack
- **Frontend Architecture**: Vanilla HTML5, Modern CSS variables, ES6+ JavaScript.
- **Graphics & Icons**: Scalable Lucide-style SVG graphics.
- **Database Engine**: Firebase Realtime Database.
- **Client Cryptography**: Native Browser Web Crypto API (SubtleCrypto).

---

## Setup and Installation

### 1. Configure Firebase
Provide your own database credentials in the `firebaseConfig` block inside `app.js`:
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

### 2. Configure Administrators (Optional)
You can easily set up administrative users and hash their passwords by running the interactive Python tool. Refer to the [Admin Setup Documentation](tools/admin-setup/README.md) for a detailed step-by-step guide.

### 3. Run Locally
Serve the application locally using any basic HTTP web server. No build steps are required.
```bash
# Using Python
python -m http.server 8000
```
Then navigate to `http://localhost:8000` in your web browser.

### 3. Deploy
The platform is fully static and can be deployed directly to platforms like Firebase Hosting, GitHub Pages, Vercel, or Netlify.
