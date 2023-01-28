// function echo(myStr) {
//     let len = myStr.length;
//     console.log(len)
//     console.log(myStr)
// }

// echo('Hello JavaScript!')
// echo('Strings are easy')

function strLen(a, b, c) {
    let len1 = a.length;
    let len2 = b.length;
    let len3 = c.length;

    let total = len1 + len2 + len3
    let avr = Math.floor(total / 3);

    console.log(total);
    console.log(avr);
}

strLen('lili', 'toshko', 'goshko')