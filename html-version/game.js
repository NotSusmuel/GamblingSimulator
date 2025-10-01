// Balance Management
let balance = 1000;
let currentBet = 0;
let currentGame = '';

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadBalance();
    updateAllBalances();
});

function loadBalance() {
    const saved = localStorage.getItem('casinoBalance');
    if (saved) {
        balance = parseInt(saved);
    } else {
        balance = 1000;
        saveBalance();
    }
}

function saveBalance() {
    localStorage.setItem('casinoBalance', balance.toString());
}

function updateAllBalances() {
    document.getElementById('main-balance').textContent = balance;
    document.getElementById('blackjack-balance').textContent = balance;
    document.getElementById('slot-balance').textContent = balance;
}

function updateBalance(amount) {
    balance += amount;
    saveBalance();
    updateAllBalances();
}

function resetBalance() {
    if (confirm('Reset balance to $1000?')) {
        balance = 1000;
        saveBalance();
        updateAllBalances();
    }
}

// Screen Management
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

function backToMenu() {
    showScreen('main-menu');
    resetBlackjack();
    resetSlotMachine();
}

// Bet Dialog
function showBetDialog(game) {
    currentGame = game;
    document.getElementById('bet-dialog').style.display = 'block';
    document.getElementById('bet-input').value = '';
    document.getElementById('bet-input').focus();
}

function closeBetDialog() {
    document.getElementById('bet-dialog').style.display = 'none';
}

function confirmBet() {
    const betInput = document.getElementById('bet-input');
    const bet = parseInt(betInput.value);
    
    if (isNaN(bet) || bet <= 0) {
        alert('Please enter a valid bet amount');
        return;
    }
    
    if (bet > 5000) {
        alert('Maximum bet is $5,000');
        return;
    }
    
    currentBet = bet;
    closeBetDialog();
    
    if (currentGame === 'blackjack') {
        showScreen('blackjack');
    } else if (currentGame === 'slotmachine') {
        showScreen('slotmachine');
    }
}

// Allow Enter key in bet dialog
document.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && document.getElementById('bet-dialog').style.display === 'block') {
        confirmBet();
    }
});

// ===== BLACKJACK GAME =====
let deck = [];
let playerCards = [];
let dealerCards = [];
let gameActive = false;

function createDeck() {
    deck = [];
    // 4 suits, 13 cards each
    for (let i = 0; i < 4; i++) {
        for (let j = 2; j <= 11; j++) {
            if (j === 11) {
                deck.push(11); // Ace
            } else if (j === 10) {
                deck.push(10); // 10
                deck.push(10); // J
                deck.push(10); // Q
                deck.push(10); // K
            } else {
                deck.push(j);
            }
        }
    }
    shuffleDeck();
}

function shuffleDeck() {
    for (let i = deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [deck[i], deck[j]] = [deck[j], deck[i]];
    }
}

function drawCardFromDeck() {
    if (deck.length === 0) {
        createDeck();
    }
    return deck.pop();
}

function getCardSum(cards) {
    return cards.reduce((sum, card) => sum + card, 0);
}

function createCardElement(value, color) {
    const card = document.createElement('div');
    card.className = `card ${color}`;
    card.textContent = value;
    return card;
}

function displayCard(container, value) {
    const color = Math.random() > 0.5 ? 'red' : 'blue';
    const card = createCardElement(value, color);
    container.appendChild(card);
}

function startBlackjack() {
    if (gameActive) return;
    
    gameActive = true;
    createDeck();
    playerCards = [];
    dealerCards = [];
    
    document.getElementById('player-cards').innerHTML = '';
    document.getElementById('dealer-cards').innerHTML = '';
    document.getElementById('game-message').textContent = '';
    
    // Deal two cards to player
    playerCards.push(drawCardFromDeck());
    playerCards.push(drawCardFromDeck());
    
    const playerContainer = document.getElementById('player-cards');
    playerCards.forEach(card => displayCard(playerContainer, card));
    
    const playerSum = getCardSum(playerCards);
    
    // Check for blackjack
    if (playerSum === 21) {
        setTimeout(() => {
            showMessage('Blackjack! You Win!');
            updateBalance(currentBet * 2);
            endGame();
        }, 500);
        return;
    } else if (playerSum > 21) {
        setTimeout(() => {
            showMessage('You Busted!');
            updateBalance(-currentBet);
            endGame();
        }, 500);
        return;
    }
    
    // Show game buttons
    document.getElementById('start-button').style.display = 'none';
    document.getElementById('draw-button').style.display = 'inline-block';
    document.getElementById('reveal-button').style.display = 'inline-block';
}

function drawCard() {
    if (!gameActive) return;
    
    const newCard = drawCardFromDeck();
    playerCards.push(newCard);
    
    const playerContainer = document.getElementById('player-cards');
    displayCard(playerContainer, newCard);
    
    const playerSum = getCardSum(playerCards);
    
    if (playerSum > 21) {
        setTimeout(() => {
            showMessage('You Busted!');
            updateBalance(-currentBet);
            endGame();
        }, 500);
    } else if (playerSum === 21) {
        setTimeout(() => {
            showMessage('Blackjack! You Win!');
            updateBalance(currentBet * 2);
            endGame();
        }, 500);
    }
}

function revealDealer() {
    if (!gameActive) return;
    
    document.getElementById('draw-button').style.display = 'none';
    document.getElementById('reveal-button').style.display = 'none';
    
    const playerSum = getCardSum(playerCards);
    const dealerContainer = document.getElementById('dealer-cards');
    
    // Dealer logic matches Python version
    if (playerSum >= 17) {
        const winOrLose = Math.random() < 0.5 ? 1 : 2;
        
        if (winOrLose === 1) {
            // Player wins
            const card1 = Math.floor(playerSum / 2) - 1;
            const card2 = Math.floor(playerSum / 2);
            
            dealerCards.push(card1);
            displayCard(dealerContainer, card1);
            
            setTimeout(() => {
                dealerCards.push(card2);
                displayCard(dealerContainer, card2);
                
                setTimeout(() => {
                    showMessage('You Win!');
                    updateBalance(currentBet * 2);
                    endGame();
                }, 1000);
            }, 1000);
        } else {
            // Player loses
            const card1 = Math.floor(playerSum / 2) + 2;
            const card2 = Math.floor(playerSum / 2);
            
            dealerCards.push(card1);
            displayCard(dealerContainer, card1);
            
            setTimeout(() => {
                dealerCards.push(card2);
                displayCard(dealerContainer, card2);
                
                setTimeout(() => {
                    showMessage('You Lose!');
                    updateBalance(-currentBet);
                    endGame();
                }, 1000);
            }, 1000);
        }
    } else {
        // Player sum < 17, dealer wins
        const card1 = Math.floor(playerSum / 2) + 2;
        const card2 = Math.floor(playerSum / 2) + 3;
        
        dealerCards.push(card1);
        displayCard(dealerContainer, card1);
        
        setTimeout(() => {
            dealerCards.push(card2);
            displayCard(dealerContainer, card2);
            
            setTimeout(() => {
                showMessage('You Lose!');
                updateBalance(-currentBet);
                endGame();
            }, 1000);
        }, 1000);
    }
}

function showMessage(message) {
    const messageEl = document.getElementById('game-message');
    messageEl.textContent = message;
    messageEl.style.animation = 'none';
    setTimeout(() => {
        messageEl.style.animation = 'pulse 0.6s ease-in-out';
    }, 10);
}

function endGame() {
    gameActive = false;
    setTimeout(() => {
        document.getElementById('start-button').style.display = 'inline-block';
        document.getElementById('draw-button').style.display = 'none';
        document.getElementById('reveal-button').style.display = 'none';
        document.getElementById('player-cards').innerHTML = '';
        document.getElementById('dealer-cards').innerHTML = '';
        document.getElementById('game-message').textContent = '';
    }, 2000);
}

function resetBlackjack() {
    gameActive = false;
    playerCards = [];
    dealerCards = [];
    document.getElementById('player-cards').innerHTML = '';
    document.getElementById('dealer-cards').innerHTML = '';
    document.getElementById('game-message').textContent = '';
    document.getElementById('start-button').style.display = 'inline-block';
    document.getElementById('draw-button').style.display = 'none';
    document.getElementById('reveal-button').style.display = 'none';
}

// ===== SLOT MACHINE GAME =====
const symbols = ['7️⃣', '🍒', '🍋', '🔔', '⭐'];
let spinning = false;

function getSymbolByNumber(num) {
    // 1=7️⃣, 2=🍒, 3=🍋, 4=🔔, 5=⭐
    return symbols[num - 1];
}

function getRandomSymbol() {
    return symbols[Math.floor(Math.random() * symbols.length)];
}

function winOrLose() {
    const result = Math.floor(Math.random() * 10) + 1;
    let a, b, c;
    
    // Match Python logic exactly
    if (result === 10) {
        // High chance to win jackpot
        a = 1;
        b = 1;
        c = Math.floor(Math.random() * 5) + 1;
    } else if (result === 9) {
        a = Math.floor(Math.random() * 5) + 1;
        b = a;
        c = Math.floor(Math.random() * 5) + 1;
    } else if (result === 8) {
        a = Math.floor(Math.random() * 5) + 1;
        b = a;
        c = Math.floor(Math.random() * 5) + 1;
    } else if (result === 7) {
        a = Math.floor(Math.random() * 5) + 1;
        b = Math.floor(Math.random() * 5) + 1;
        c = b;
    } else if (result === 6) {
        // You can't win
        a = 1;
        b = 1;
        c = Math.floor(Math.random() * 4) + 2;
    } else if (result === 5) {
        a = 1;
        b = Math.floor(Math.random() * 5) + 1;
        c = Math.floor(Math.random() * 5) + 1;
    } else if (result === 4) {
        a = Math.floor(Math.random() * 4) + 2;
        b = 1;
        c = Math.floor(Math.random() * 5) + 1;
    } else if (result === 3) {
        a = 1;
        b = 1;
        c = Math.floor(Math.random() * 4) + 2;
    } else {
        a = Math.floor(Math.random() * 5) + 1;
        b = Math.floor(Math.random() * 5) + 1;
        c = Math.floor(Math.random() * 5) + 1;
    }
    
    return [a, b, c];
}

function findPrize(a, b, c) {
    // Match Python logic exactly
    if (a === 1 && b === 1 && c === 1) {
        return currentBet * 10; // Jackpot
    } else if (a === 1 || b === 1 || c === 1) {
        return 0;
    } else if (a === 1 && b === 1) {
        return 0;
    } else if (a === 1 && c === 1) {
        return 0;
    } else if (b === 1 && c === 1) {
        return 0;
    } else if (a === b && b === c) {
        return currentBet * 5; // Three matching
    } else if (a === b || a === c || b === c) {
        return currentBet * 2; // Two matching
    } else {
        return 0;
    }
}

function setSlotSymbols(row1, row2, row3) {
    const rows = [
        document.getElementById('slot-row-1'),
        document.getElementById('slot-row-2'),
        document.getElementById('slot-row-3')
    ];
    
    const allSymbols = [row1, row2, row3];
    
    rows.forEach((row, rowIndex) => {
        const symbols = row.querySelectorAll('.slot-symbol');
        symbols.forEach((symbol, colIndex) => {
            symbol.textContent = allSymbols[rowIndex][colIndex];
        });
    });
}

async function animateSpin(finalResult) {
    const rows = [
        document.getElementById('slot-row-1'),
        document.getElementById('slot-row-2'),
        document.getElementById('slot-row-3')
    ];
    
    // Fast spin animation - each symbol animates independently
    for (let i = 0; i < 20; i++) {
        rows.forEach(row => {
            const symbols = row.querySelectorAll('.slot-symbol');
            symbols[0].textContent = getRandomSymbol();
            symbols[1].textContent = getRandomSymbol();
            symbols[2].textContent = getRandomSymbol();
        });
        await sleep(50);
    }
    
    // Slow down - each symbol still independent
    for (let i = 0; i < 10; i++) {
        rows.forEach(row => {
            const symbols = row.querySelectorAll('.slot-symbol');
            symbols[0].textContent = getRandomSymbol();
            symbols[1].textContent = getRandomSymbol();
            symbols[2].textContent = getRandomSymbol();
        });
        await sleep(100);
    }
    
    // Get symbol references for easier access
    const [a, b, c] = finalResult;
    const row1Symbols = rows[0].querySelectorAll('.slot-symbol');
    const row2Symbols = rows[1].querySelectorAll('.slot-symbol');
    const row3Symbols = rows[2].querySelectorAll('.slot-symbol');
    
    // Set column 0 to result in row 1, other columns random
    row3Symbols[0].textContent = row2Symbols[0].textContent;
    row3Symbols[1].textContent = row2Symbols[1].textContent;
    row3Symbols[2].textContent = row2Symbols[2].textContent;
    row2Symbols[0].textContent = row1Symbols[0].textContent;
    row2Symbols[1].textContent = row1Symbols[1].textContent;
    row2Symbols[2].textContent = row1Symbols[2].textContent;
    row1Symbols[0].textContent = getSymbolByNumber(a);
    row1Symbols[1].textContent = getRandomSymbol();
    row1Symbols[2].textContent = getRandomSymbol();
    await sleep(100);
    
    // Scroll down - now row 2 has result in column 0
    row3Symbols[0].textContent = row2Symbols[0].textContent;
    row3Symbols[1].textContent = row2Symbols[1].textContent;
    row3Symbols[2].textContent = row2Symbols[2].textContent;
    row2Symbols[0].textContent = row1Symbols[0].textContent;
    row2Symbols[1].textContent = row1Symbols[1].textContent;
    row2Symbols[2].textContent = row1Symbols[2].textContent;
    row1Symbols[0].textContent = getRandomSymbol();
    row1Symbols[1].textContent = getRandomSymbol();
    row1Symbols[2].textContent = getRandomSymbol();
    await sleep(100);
    
    // Continue animating columns 1 and 2 only
    for (let i = 0; i < 5; i++) {
        row3Symbols[1].textContent = row2Symbols[1].textContent;
        row3Symbols[2].textContent = row2Symbols[2].textContent;
        row2Symbols[1].textContent = row1Symbols[1].textContent;
        row2Symbols[2].textContent = row1Symbols[2].textContent;
        row1Symbols[1].textContent = getRandomSymbol();
        row1Symbols[2].textContent = getRandomSymbol();
        await sleep(100);
    }
    
    // Set column 1 to result in row 1
    row3Symbols[1].textContent = row2Symbols[1].textContent;
    row3Symbols[2].textContent = row2Symbols[2].textContent;
    row2Symbols[1].textContent = row1Symbols[1].textContent;
    row2Symbols[2].textContent = row1Symbols[2].textContent;
    row1Symbols[1].textContent = getSymbolByNumber(b);
    row1Symbols[2].textContent = getRandomSymbol();
    await sleep(100);
    
    // Scroll down - now row 2 has result in columns 0 and 1
    row3Symbols[1].textContent = row2Symbols[1].textContent;
    row3Symbols[2].textContent = row2Symbols[2].textContent;
    row2Symbols[1].textContent = row1Symbols[1].textContent;
    row2Symbols[2].textContent = row1Symbols[2].textContent;
    row1Symbols[1].textContent = getRandomSymbol();
    row1Symbols[2].textContent = getRandomSymbol();
    await sleep(200);
    
    // Continue animating column 2 only
    for (let i = 0; i < 5; i++) {
        row3Symbols[2].textContent = row2Symbols[2].textContent;
        row2Symbols[2].textContent = row1Symbols[2].textContent;
        row1Symbols[2].textContent = getRandomSymbol();
        await sleep(500);
    }
    
    // Set column 2 to result in row 1
    row3Symbols[2].textContent = row2Symbols[2].textContent;
    row2Symbols[2].textContent = row1Symbols[2].textContent;
    row1Symbols[2].textContent = getSymbolByNumber(c);
    await sleep(200);
    
    // Final scroll down - now row 2 has complete result
    row3Symbols[2].textContent = row2Symbols[2].textContent;
    row2Symbols[2].textContent = row1Symbols[2].textContent;
    row1Symbols[2].textContent = getRandomSymbol();
    await sleep(1000);
    
    // Highlight winning row
    await sleep(500);
    const winningRow = document.getElementById('slot-row-2');
    winningRow.style.background = 'rgba(233, 69, 96, 0.4)';
    winningRow.style.animation = 'glow 1s ease-in-out 2';
    
    await sleep(1000);
    winningRow.style.background = 'rgba(233, 69, 96, 0.2)';
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function pullLever() {
    if (spinning) return;
    
    spinning = true;
    const lever = document.getElementById('lever');
    lever.classList.add('pulling');
    lever.disabled = true;
    
    // Deduct bet
    updateBalance(-currentBet);
    
    // Determine result
    const result = winOrLose();
    
    // Animate
    await animateSpin(result);
    
    // Calculate prize
    const prize = findPrize(result[0], result[1], result[2]);
    
    // Update balance and show message
    if (prize > 0) {
        updateBalance(prize);
        const messageEl = document.getElementById('slot-message');
        if (prize === currentBet * 10) {
            messageEl.textContent = `🎉 JACKPOT! Won $${prize}! 🎉`;
        } else if (prize === currentBet * 5) {
            messageEl.textContent = `🎊 Three of a Kind! Won $${prize}! 🎊`;
        } else {
            messageEl.textContent = `✨ Won $${prize}! ✨`;
        }
        messageEl.style.animation = 'pulse 0.6s ease-in-out 3';
    } else {
        document.getElementById('slot-message').textContent = 'Try Again!';
    }
    
    setTimeout(() => {
        document.getElementById('slot-message').textContent = '';
    }, 3000);
    
    lever.classList.remove('pulling');
    lever.disabled = false;
    spinning = false;
}

function resetSlotMachine() {
    spinning = false;
    document.getElementById('slot-message').textContent = '';
    const lever = document.getElementById('lever');
    lever.classList.remove('pulling');
    lever.disabled = false;
    
    // Reset to default symbols
    setSlotSymbols(
        ['🍒', '🍋', '⭐'],
        ['🍋', '🍋', '🍋'],
        ['⭐', '⭐', '⭐']
    );
}
