'use strict';

var c, ctx, w, h, characters, nextframe;

(function () {
    Math.randomInt = function (min, max) {
        return Math.floor(Math.random() * (max - min)) + min;
    };
    Math.randomDec = function (min, max, decimals) {
        return (Math.random() * (max - min) + min).toFixed(decimals || 2);
    };
    Math.randomList = function (list) {
        return list[Math.randomInt(0, list.length)];
    };
})();

function init() {
    c = document.getElementById('c');
    c.width = w = window.innerWidth;
    c.height = h = window.innerHeight;
    ctx = c.getContext('2d');
    
    characters = [];
    var alphabets = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ऌ', 'ऍ', 'ए', 'ऐ', 'ऑ', 'ऒ', 'ओ', 'औ', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ळ', 'क', 'ष', 'ज', 'ञ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    var numCharacters = 180;
    var radius = Math.min(w, h) / 2;
    var angleStep = 2 * Math.PI / numCharacters;

    for (var i = 0; i < numCharacters; i++) {
        var angle = i * angleStep;
        var x = w / 2 + radius * Math.cos(angle);
        var y = h / 2 + radius * Math.sin(angle);
        characters[i] = new Character(Math.randomList(alphabets), x, y);
        characters[i].init();
    }
    
    loop();
}

function loop() {
    ctx.clearRect(0, 0, w, h);
    for (var i = 0; i < characters.length; i++) {
        if (characters[i].isOut()) {
            characters[i].init();
        }
        characters[i].update();
        characters[i].draw();
    }
    
    nextframe = requestAnimationFrame(loop);
}

function Character(char, x, y) {
    this.char = char;
    this.x = x;
    this.y = y;
    this.s = Math.randomDec(.2, 2);
    this.a = Math.randomDec(0, 2*Math.PI);
    this.alive = true;
    this.color = `rgb(${Math.randomInt(0, 255)}, ${Math.randomInt(0, 255)}, ${Math.randomInt(0, 255)})`;
    
    this.init = function () {
        this.x = Math.randomInt(0, w);
        this.y = Math.randomInt(0, h);
        this.s = Math.randomDec(.2, 2);
        this.a = Math.randomDec(0, 2*Math.PI);
        this.alive = true;
        this.color = `rgb(${Math.randomInt(0, 255)}, ${Math.randomInt(0, 255)}, ${Math.randomInt(0, 255)})`;
    };
}

Character.prototype.kill = function () {
    this.alive = false;
};

Character.prototype.isOut = function () {
    return (this.x+10 < 0
            || this.x-10 > w
            || this.y+10 < 0
            || this.y-10 > h);
};

Character.prototype.update = function () {
    this.x += Math.cos(this.a) * this.s;
    this.y += Math.sin(this.a) * this.s;
};

Character.prototype.draw = function () {
    ctx.save();
    ctx.font = '20px Arial';
    ctx.fillStyle = this.color;
    ctx.translate(this.x, this.y);
    ctx.rotate(this.a);
    ctx.fillText(this.char, -10, 10); // Adjust the position as needed
    ctx.restore();
};

// Ensure init is called after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    init();
});

window.addEventListener('resize', function () {
    cancelAnimationFrame(nextframe);
    init();
});
