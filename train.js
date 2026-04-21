//MITASK-C
/*Shunday function tuzing, u 2ta string parametr ega bolsin, 
hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;*/
//SOLUTION
//DEFINE
const checkContent = (string1, string2) => {
    if (typeof string1 != 'string' || typeof string2 != 'string') {
        return "Please enter string arguments"
    }

    if (string1.length != string2.length) {
        return false
    }

    let letter = ""
    for (const char of string1) {
        for (const ele of string2) {
            if (char === ele) {
                letter += char
            }
        }
    }
    return true
}

//CALL
const mitaskc = checkContent("muhammad", "mmmdahau")
console.log(mitaskc)




//MITASK-B
/*Shunday function tuzing, u 1ta string parametrga ega bolsin, 
hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.*/
//SOLUTION
//DEFINE
// const numberCount = (numtext) => {
//     let count = 0;
//     for (const char of numtext) {
//         if (Number(char) == char) {
//             count += 1;
//         }
//     }
//     return count
// }

// //CALL
// const result = numberCount('ad2a54y79wet0sfgb9bdj7df890')
// console.log(result)



// MITASK-A
/*
Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi 
letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/


//SOLUTIION
// DEFINE
/*
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
*/