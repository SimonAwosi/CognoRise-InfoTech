// Select the canvas
const canvas = document.getElementById("pongCanvas");
const context = canvas.getContext("2d");

// Create the paddles and ball
const player = {
    x: 10,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    color: "WHITE",
    score: 0
};

const ai = {
    x: canvas.width - 20,
    y: canvas.height / 2 - 50,
    width: 10,
    height: 100,
    color: "WHITE",
    score: 0
};

const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    radius: 10,
    speed: 5,
    velocityX: 5,
    velocityY: 5,
    color: "WHITE"
};

// Draw the paddles and ball
function drawRect(x, y, w, h, color) {
    context.fillStyle = color;
    context.fillRect(x, y, w, h);
}

function drawCircle(x, y, r, color) {
    context.fillStyle = color;
    context.beginPath();
    context.arc(x, y, r, 0, Math.PI * 2, false);
    context.closePath();
    context.fill();
}

function drawText(text, x, y, color) {
    context.fillStyle = color;
    context.font = "45px Arial";
    context.fillText(text, x, y);
}

// Reset the ball after scoring
function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.velocityX = -ball.velocityX;
    ball.speed = 5;
}

// Collision detection
function collision(b, p) {
    p.top = p.y;
    p.bottom = p.y + p.height;
    p.left = p.x;
    p.right = p.x + p.width;

    b.top = b.y - b.radius;
    b.bottom = b.y + b.radius;
    b.left = b.x - b.radius;
    b.right = b.x + b.radius;

    return p.left < b.right && p.top < b.bottom && p.right > b.left && p.bottom > b.top;
}

// Update the ball and AI movement
function update() {
    // Move the ball
    ball.x += ball.velocityX;
    ball.y += ball.velocityY;

    // AI paddle movement (basic AI logic: follow the ball)
    ai.y += (ball.y - (ai.y + ai.height / 2)) * 0.1;

    // Ball collision with top and bottom walls
    if (ball.y - ball.radius < 0 || ball.y + ball.radius > canvas.height) {
        ball.velocityY = -ball.velocityY;
    }

    // Ball collision with player paddle
    if (collision(ball, player)) {
        ball.velocityX = -ball.velocityX;
        ball.speed += 0.5;
    }

    // Ball collision with AI paddle
    if (collision(ball, ai)) {
        ball.velocityX = -ball.velocityX;
        ball.speed += 0.5;
    }

    // Scoring
    if (ball.x - ball.radius < 0) {
        ai.score++;
        resetBall();
    } else if (ball.x + ball.radius > canvas.width) {
        player.score++;
        resetBall();
    }
}

// Listen for player paddle movement
canvas.addEventListener("mousemove", movePaddle);
function movePaddle(evt) {
    let rect = canvas.getBoundingClientRect();
    player.y = evt.clientY - rect.top - player.height / 2;
}

// Render the game objects
function render() {
    // Clear the canvas
    drawRect(0, 0, canvas.width, canvas.height, "#000");

    // Draw paddles and ball
    drawRect(player.x, player.y, player.width, player.height, player.color);
    drawRect(ai.x, ai.y, ai.width, ai.height, ai.color);
    drawCircle(ball.x, ball.y, ball.radius, ball.color);

    // Draw scores
    drawText(player.score, canvas.width / 4, canvas.height / 5, "WHITE");
    drawText(ai.score, 3 * canvas.width / 4, canvas.height / 5, "WHITE");
}

// Game loop
function game() {
    update();
    render();
}

// Run the game at 50 frames per second
const fps = 50;
setInterval(game, 1000 / fps);
