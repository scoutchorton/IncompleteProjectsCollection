var version = "0.1.4";

/*

 _____  _____    ___  _____
/ __  \|  _  |  /   ||  _  |
`' / /'| |/' | / /| | \ V /
  / /  |  /| |/ /_| | / _ \
./ /___\ |_/ /\___  || |_| |
\_____/ \___/     |_/\_____/

Coded by scoutchorton

Features:
    - 0.1.0
        Assigned color choices
    - 0.1.2
        Random placement of new tiles
    - 0.1.3
        Colors by numbers
    - 0.1.4
        Numbers decrease in size depending on length (1000 would be smaller than 10 in order to fit it in the blocks)
    - 0.1.5
        Colors range based on number

Todos:
    * Combining tiles
    * Adding #flair

*/



















//Variables
var blocks = [
[2, 4, 8, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 2072]
];
var colors = {"ora": color(233, 84, 32), "amb": color(94, 39, 80), "blo":[233,134,32]};
//Low range = http://www.colorhexa.com/e98620 middle - (50)
//Middle = http://www.colorhexa.com/e95420
//High range = http://www.colorhexa.com/e92220 middle + (50)
var baseColor = colors.amb;
var colorRatio = 11/255;

//Preferences
var settings = {"padding":58, "center":[110, 150]};
textFont(createFont("monospace"));
textAlign(CENTER);

//Functions
var multiTest = function(n1, n2) {
    if(n1 === n2) {
        return true;
    } else {
        return false;
    }
};

var drawBlocks = function() {
    for(var yy=0; yy<blocks.length; yy++){
        for(var xx=0; xx<blocks[yy].length; xx++){
            var pos = [((settings.center[0])-((settings.padding+xx)/2))+xx+(xx*settings.padding), ((settings.center[1])-((settings.padding+xx)/2))+yy+(yy*settings.padding)];
            if(blocks[yy][xx] !== 0) {
                fill(colors.blo[0], colors.blo[1]+((colorRatio+0.5)*50), colors.blo[2]);
            } else {
                noFill();
            }
            var asdb = 1;
            rect(pos[0], pos[1], 50, 50, 15);
            fill(baseColor);
            textSize(30-(((blocks[yy][xx].toString()).length)*3));
            text(blocks[yy][xx], pos[0]+25, pos[1]+35-((blocks[yy][xx].toString()).length));
        }
    }
};

var genRan = function() {
    var x = ceil(random(-1, 3));
    var y = ceil(random(-1, 3));
    if(blocks[y][x] !== 0){
        genRan();
    } else {
        blocks[y][x] = 2;
    }
};

var turn = function() {
    var took = true;
    if(keyCode === UP) {

    } else if(keyCode === DOWN) {

    } else if(keyCode === LEFT) {

    } else if(keyCode === RIGHT) {

    } else {
       took = false;
    }
    if(took === true) {
        genRan();
    }
};

var keyReleased = function() {
    turn();
};

var draw = function() {
    background(baseColor);
    fill(255, 0, 0);
    textSize(10);
    textAlign(LEFT);
    fill(colors.ora);
    text("Version " + version, 5, 395);
    textAlign(CENTER);
    drawBlocks();
};
