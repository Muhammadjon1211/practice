async function division(a, b) {
    return new Promise((resolve,reject) => {
        if (b===0) {
            reject("Not divided by zero.");
        } else {
            setTimeout(function() {
                resolve(a&b)
            }, 2000)
        }
    })
}


division(10,3).then(data => {
    console.log("RESULT:", data)
}).catch(err=>{
    console.log("Error division:", err)
});