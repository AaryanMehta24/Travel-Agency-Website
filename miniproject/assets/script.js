let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');
let formBtn = document.querySelector('#login-btn');
let loginBtn = document.querySelector('#loginBtn');
let loginForm = document.querySelector('.login-form-container');
let registerBtn = document.querySelector('#registerBtn');
let registerForm = document.querySelector('#register-form-container');
let formClose = document.querySelector('#form-close');
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');
let videoBtn = document.querySelectorAll('.vid-btn');

window.onscroll = () =>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    loginForm.classList.remove('active');
}

menu.addEventListener('click', () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
});

searchBtn.addEventListener('click', () =>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');
});

formBtn.addEventListener('click', () =>{
    loginForm.classList.add('active');
});

formClose.addEventListener('click', () =>{
    loginForm.classList.remove('active');
});

function Toggle(){
  // let create = document.getElementById('createacc');
  registerForm.classList.add('active');
}
// registerBtn.addEventListener('click', () =>{
//     registerForm.classList.remove('active');
//     loginForm.classList.add('active');
// });

loginBtn.addEventListener('click', () =>{
    // document.LoginForm.user_email.value="";
    // document.LoginForm.user_password.value="";
    loginForm.classList.remove('active');
    alert("Login Sucessfull!");
    // confirm('Are You Sure, you want to submit?',"");

});
registerBtn.addEventListener('click' , () =>{
  document.RegisterationForm.Password.value = "";
  document.RegisterationForm.email.value ="";
  document.RegisterationForm.password2.value="";
  document.RegisterationForm.username.value="";
  document.RegisterationForm.first_name.value="";
  document.RegisterationForm.last_name.value=""

} );
//Validation
function validate(){
  //Email Validation
   var email = document.RegisterationForm.email.value ;
   var ContactNo = document.RegisterationForm.ContactNo.value ;
   var Passwd    = document.RegisterationForm.password1.value ;
   var ConfirmPasswd    = document.RegisterationForm.password2.value ;
   var name    = document.RegisterationForm.first_name.value ;

   if(email.indexOf('@')<=0){
     document.getElementById("Message").innerHTML=" Invalid Email ID";
     return false;
   }
   if(email.charAt(email.length-4)!='.'){
     document.getElementById("Message").innerHTML=" Invalid Email ID";
     return false;
   }
   if(email=="" || ContactNo=="" || Passwd==" " || ConfirmPasswd=="" || name==" " ){
    document.getElementById("Message").innerHTML=" Enter All Details";
    return false;
   }
   if(Passwd!=ConfirmPasswd){
    document.getElementById("Message").innerHTML="Incorrect Password";
    return false;
   }
   if(ContactNo.toString().length<=9){
    document.getElementById("Message").innerHTML="Invalid ContactNo.";
    return false;
   }
}
videoBtn.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#video-slider').src = src;
    });
});

var swiper = new Swiper(".review-slider", {
    spaceBetween: 20,
    loop:false,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    breakpoints: {
        640: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        1024: {
          slidesPerView: 3,
        },
    },
});

var swiper = new Swiper(".brand-slider", {
    spaceBetween: 20,
    loop:false,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    breakpoints: {
        450: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        991: {
          slidesPerView: 4,
        },
        1200: {
          slidesPerView: 5,
        },
      },
});