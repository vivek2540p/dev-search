// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWrapper=document.querySelector('.alert')
let alertclose=document.querySelector('.alert__close')
alertclose.addEventListener('click',function(){
})

if(alertWrapper){
  console.log("hiii");
  alertclose.addEventListener('click',function(){
    console.log("hii111");
    alertWrapper.style.display = 'none'
    })
}