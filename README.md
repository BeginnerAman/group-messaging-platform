# GroupChat 💬

A real-time group chat application built with Firebase and modern web technologies.

## Features

### Core Chat Features
- **Real-time Messaging**: Send and receive messages instantly using Firebase Realtime Database
- **User Presence**: See who's online in real-time
- **Typing Indicators**: Shows when other users are typing
- **Reply to Messages**: Quote specific messages with reply functionality
- **Message Reactions**: Add emoji reactions to any message (❤️, 😂, 😮, 🔥, 👍, etc.)
- **Edit & Delete Messages**: Users can edit their own messages, admins can edit any message
- **Emoji Picker**: Quick access to 60+ emojis

### Admin Features
- **Mute Chat**: Disable messaging for all regular users
- **Mute Individual Users**: Temporarily silence specific users for a set duration
- **Clear Chat**: Remove all messages at once
- **Pin Messages**: Highlight important messages with a pin bar at the top
- **Send Announcements**: Broadcast important information to all users
- **Message Highlighting**: Highlight important messages with special styling
- **Special Effects**: Trigger heart or confetti animations for celebrations

### UI/UX Features
- **Beautiful Particle Background**: Animated particle canvas on join screen
- **Smooth Animations**: Glassmorphic design with GSAP animations
- **Mobile Responsive**: Works perfectly on phones, tablets, and desktops
- **Dark Theme**: Modern dark interface with accent colors
- **Side Panels**: Online users list and admin controls in slide-out panels
- **Toast Notifications**: Informative notifications for events and admin actions

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (54.6% JavaScript, 36% CSS, 9.4% HTML)
- **Backend/Database**: Firebase Realtime Database
- **Animations**: GSAP (GreenSock Animation Platform)
- **Fonts**: DM Sans, Syne from Google Fonts

## How to Use

### 1. Join the Chat
- Enter your name (no account needed)
- Click "Join Chat" to enter instantly
- That's it! No signup, no passwords required

### 2. Send Messages
- Type your message in the input box
- Press Enter or click the send button
- Use the emoji button (😊) to add emojis to your message

### 3. Interact with Messages
- **Reply**: Click the reply button (↩) to quote a message
- **React**: Click the react button (😊) to add an emoji reaction
- **Edit**: Click the pencil button (✏️) to edit your message
- **Delete**: Click the trash button (🗑️) to delete your message
- **Pin** (Admin only): Click the pin button to highlight a message

### 4. Admin Functions
Users with admin access get extra powers:
- Mute/unmute the entire chat
- Mute individual users temporarily
- Clear all messages
- Pin important messages
- Send announcements
- Trigger celebratory animations

## Special Features

### Message Highlighting
Admins can highlight next message with special styling to draw attention.

### Pin Bar
When a message is pinned, it appears at the top of the chat for everyone to see. Click the pin bar to scroll to that message.

### Effects
Trigger heart animations ❤️ or confetti 🎉 to celebrate with the group.

### Typing Indicators
See who's currently typing before their message arrives.

## File Structure

```
├── index.html          # Main HTML file with UI structure
├── app.js              # JavaScript logic (39KB - chat functionality)
├── style.css           # Styling and animations (26KB)
└── README.md           # This file
```

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Installation & Deployment

1. Clone the repository
2. No installation needed - it's a static web app!
3. Open `index.html` in your browser or deploy to GitHub Pages

The app works completely client-side with Firebase as the backend.

## Notes

- Messages are stored in Firebase Realtime Database
- Online presence automatically clears when you close the browser
- Muted status is temporary and expires after the set duration
- All timestamps are in local timezone

---

**Version**: Enhanced Edition  
**Created**: April 2026  
**Status**: Active
