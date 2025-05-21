console.log("test oggetti");

class Punto{
    constructor(x,y){
        this.x = x;
        this.y = y;
    }

    move(width,height){
        this.x+=width;
        this.y+=height;
    }

    print(){
        console.log(this.x,this.y);
    }
}

//funzionamento oggetti
let p1 = new Punto(10,20);
console.log("posizione p1");
p1.print();
p1.move(5,-5);
p1.print();

let p2 = new Punto(0,0);

p1 = p2;

p2.move(100,100);

p1.print() //?? 0,0
p2.print() //?? 100,100

p1.move()

//funzionamento tipi primitivi
let x = 10;

let y = 20;

const z = x;
x = y;
y= z;

x = y;

y = 15;

console.log(x,y); //x=20 y=15

const message = "tra poco intervallo!!!";
