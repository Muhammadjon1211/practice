
async function division(a, b) {
        if (b===0) {
            throw new Error("Nod divided by ZERO.")
        } else {
            return a%b
        }
    }

async function run() {
    let result = await division(10,3);
    console.log(result)

    result = await division(10,4);
    console.log(result)

    result = await division(10,5);
    console.log(result)
}
run()