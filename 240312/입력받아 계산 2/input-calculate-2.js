const fs = require("fs");
let a = fs.readFileSync(0).toString();

let a1 = a.split(" ")
let num1 = parseInt(a1[0])
let num2 = parseInt(a1[1])

console.log(num1 * num2)