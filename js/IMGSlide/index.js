/* CHANGING IMAGES AUTOMATICALLY IN THE HOME PAGE*/

let landingImg = document.querySelector('.image-container') ;
let countnumber = document.querySelector('#number');
let imgArray = [];
let numOfPics = 5; // the number of images 
// NB images must be given names such as img1,img2,img3... 

for (let i = 1; i <= numOfPics; i++) {
  imgArray.push(`img${[i]}`);    
}

let creatImg = document.createElement("img"); //creating img element
let count = 0;

setInterval(() => {
//making the src attribute of the img element take the location of the images to be displayed
  creatImg.src = `./public/img/${imgArray[count]}.png`;
  landingImg.appendChild(creatImg); // appending the created img element to the class .img
  countnumber.innerHTML =  `0${count + 1} <sup> /${numOfPics} </sup>`;
  count++;
  if (count == numOfPics) return count = 0;
  
},10000)

/* END OF THE IMAGE CHANGER */