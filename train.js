// MITASK-A
/*
Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi 
letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/


//SOLUTIION
// DEFINE
const letterCount = (letter, word) => {
    if (typeof letter !== "string" || letter.length !== 1) {
        console.log("Please enter a single letter as a first argument")
    }

    if (typeof word !== 'string') {
        console.log("Please enter a word as a second argument")
    }

    let number = 0

    for (let i = 0; i < word.length; i++) {
        if (word[i].toLowerCase() === letter.toLowerCase()) {
            number += 1;
        }
    }

    return number
}

//CALL
const result = letterCount("m", "muhammad")
console.log(result)