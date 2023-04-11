const enquiryFormPopup = document.querySelector(".enquiry-form-popup");
const closeForm = document.querySelector(".close-form");
const enquirybtn = document.querySelectorAll("#donate-to-nlr");
const background = document.querySelector(".background");
const mouse = document.querySelector(".cursor-close");

enquirybtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    enquiryFormPopup.classList.toggle("active");
    background.classList.toggle("active");
  });
});

closeForm.addEventListener("click", () => {
  enquiryFormPopup.classList.remove("active");
  background.classList.remove("active");
});

background.addEventListener("click", () => {
  enquiryFormPopup.classList.remove("active");
  background.classList.remove("active");
});

document.addEventListener("mousemove", (e) => {
  let x = e.x;
  let y = e.y;

  mouse.style.top = y + "px";
  mouse.style.left = x + "px";
});
