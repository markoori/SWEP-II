//single page application
let SPA = document.querySelector('SPA') as HTMLElement;

console.log(SPA.firstElementChild)


//using a function
// function SPA(arg:string,num:number){
//     let pageList:string[];
//     for (let i = 0; i < num; i++) {
//         pageList.push(`page${i}`)      
//     }

//     pageList.filter(page => page != arg).forEach(element => {
//       ( document.querySelector(`${element}`) as HTMLStyleElement ).style.display = 'none';
//     });
//     ( document.querySelector(`${arg}`) as HTMLStyleElement ).style.display = 'block';
// }