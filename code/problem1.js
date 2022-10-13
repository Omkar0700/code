class reactangle{
    constructor(length, breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    area(){
        return this.length * this.breadth
    }
}

function button(){
    let l = document.getElementById('length').value
    let b = document.getElementById('breadth').value
    console.log(l,b)
    const a = new reactangle(l,b);
    document.getElementById('ans').innerHTML = `<h1>The Area of the reactangle is ${a.area()}</h1>`
}