const galleryBtns = document.querySelectorAll("#galleryBtn");
const galleryPopup = document.querySelector(".gallery-popup");
const galleryClose = document.querySelector(".close-gallery-btn");
const galleryBg = document.querySelector(".gallery-bg");

galleryBtns.forEach((galleryBtn) => {
  galleryBtn.addEventListener("click", () => {
    galleryPopup.classList.add("active");
  });
});

galleryClose.addEventListener("click", () => {
  galleryPopup.classList.remove("active");
});

galleryBg.addEventListener("click", () => {
  galleryPopup.classList.remove("active");
});
