const fs = require("fs");
let input = fs.readFileSync(0).toString().split("\n");


let l1 = parseInt(input[0]);
let l2 = parseInt(input[1]);

console.log(l1 * l2)