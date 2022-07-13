const sign_in_btn = document.querySelector ('#sign-in-button');
const sign_up_btn = document.querySelector ('#sign-up-button');
const container = document.querySelector ('.container');
sign_up_btn.addEventListener('click', () => {
      container.classList.add('sign-up-mode');
  });
sign_in_btn.addEventListener('click', () => {
      container.classList.remove('sign-up-mode');
  });


let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navlist');

menu.onclick = () => {
  menu.classList.toggle('bx-x');
  navlist.classList.toggle('open')
};

// var filter = document.querySelector(".filter");

// var dropdown_li_items = document.querySelectorAll(".dropdown ul li label");

// var checkbox_items = document.querySelectorAll(".dropdown ul li input");

// var filter_text = document.querySelector(".filter .text");

// filter.addEventListener("click", function(){
//   filter.classList.toggle("active");
// })

// dropdown_li_items.forEach(function(item, index){
//   item.addEventListener("click", function(){

//       checkbox_items.forEach(function(c_item, c_index){
//         if(index == c_index){
//           var item_text = item.querySelector(".text").innerText;
//           filter_text.innerText = item_text;
//           c_item.checked = true;
//         }
//         else{
//             c_item.checked = false;
//         }
//       });

//       filter.classList.remove("active");
//   })
// });