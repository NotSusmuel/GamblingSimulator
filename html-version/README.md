# HTML Casino Royale 🎰

A modern, sleek HTML5 version of the Gambling Simulator with smooth animations and the same winning mechanics as the Python version.

## Features ✨

- **🎨 Modern Design**: Sleek, responsive interface with smooth CSS animations
- **🎰 Slot Machine**: Spin the reels with realistic reel-stop animations
- **♠️ Blackjack**: Classic card game with smooth card dealing animations
- **💰 Persistent Balance**: Your balance is saved in localStorage
- **📱 Responsive**: Works on desktop and mobile devices
- **⚡ Fast & Smooth**: CSS-powered animations with no external dependencies

## How to Play

1. Open `index.html` in any modern web browser
2. Select a game from the main menu
3. Place your bet (max $5,000)
4. Play and watch your balance change!

You start with $1,000 and can go into infinite debt!

## Game Mechanics

### Blackjack ♠️
- **Start**: Deal two cards to yourself
- **Draw Card**: Add another card to your hand
- **Reveal Dealer**: See if you beat the dealer
- **Win Conditions**: 
  - Get 21 (Blackjack) to win 2x your bet
  - If your total is 17+, you have a 50% chance to beat the dealer
  - Bust (over 21) and you lose your bet

### Slot Machine 🎰
- **Pull the Lever**: Click the red ball to spin
- **Symbols**: 7️⃣ (lucky seven), 🍒 (cherry), 🍋 (lemon), 🔔 (bell), ⭐ (star)
- **Winning Combinations** (middle row):
  - **7️⃣ 7️⃣ 7️⃣**: 10x bet (Jackpot!)
  - **Three matching symbols**: 5x bet
  - **Two matching symbols**: 2x bet
  - **Any 7️⃣ present**: No win (unless all three)

## Technical Details

### Same Winning Chances as Python Version
The HTML version uses the exact same probability logic as the Python version:

**Slot Machine Odds:**
- 10% chance for potential jackpot setup (result = 10)
- 20% chance for two matching symbols (results 7-9)
- 60% chance for losing combination (results 1-6)
- 10% tease with two 7️⃣s but third different (result = 6)

**Blackjack Odds:**
- 50/50 chance to beat dealer when you stand with 17+
- Automatic win with 21
- Automatic loss when busting (over 21)

### Technologies Used
- **HTML5**: Semantic structure
- **CSS3**: Modern styling with animations
- **Vanilla JavaScript**: Game logic (no frameworks)
- **localStorage API**: Balance persistence

### Animations
- **Fade In**: Smooth screen transitions
- **Slide In**: Button entrance animations
- **Spin**: Slot machine reel animations
- **Pulse**: Message emphasis effects
- **Glow**: Winning highlight effects
- **Lever Pull**: Realistic lever animation

## File Structure
```
html-version/
├── index.html    # Main HTML structure
├── styles.css    # Styling and animations
├── game.js       # Game logic and mechanics
└── README.md     # This file
```

## Browser Compatibility

Works on all modern browsers:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Advantages Over Python Version

1. **No Installation Required**: Just open in a browser
2. **Cross-Platform**: Works on any device with a browser
3. **Smoother Animations**: CSS-powered transitions
4. **Better Accessibility**: Responsive design for mobile
5. **Faster Loading**: No Python runtime needed
6. **Easy to Share**: Just send the HTML file

## Design

The HTML version maintains the same color scheme as the Python version:
- **Primary Background**: `#1a1a2e` (Dark Blue-Purple)
- **Secondary Background**: `#0f3460` (Deep Blue)
- **Accent Color**: `#e94560` (Vibrant Pink/Red)
- **Secondary Accent**: `#533483` (Purple)
- **Text Color**: `#eef4ed` (Off-White)
- **Border/Divider**: `#16213e` (Medium Blue)

The UI is sleeker with:
- Rounded corners on all elements
- Smooth hover effects
- Animated transitions
- Modern typography
- Professional spacing

## License

Same as parent project.

---

Enjoy gambling responsibly (with fake money)! 🎰✨
