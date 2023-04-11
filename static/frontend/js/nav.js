// nav dropdown
const dropDownBtn = document.querySelectorAll(".drop-down");
const drop = document.querySelectorAll(".nav-sec .drop");

dropDownBtn.forEach((btn, idx) => {
  $(btn).hover(() => {
    drop[idx].classList.toggle("active");
  });
});

// admission-open
const admissionBtn = document.querySelectorAll("#admission-btn");
const admissionList = document.querySelector(".admission-open .list");

admissionBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    admissionList.classList.toggle("active");
  });
});

// side-nav-dropdown
const sideNavDropBtns = document.querySelectorAll(".side-nav-drop-btn");
const sideNavDrops = document.querySelectorAll(".side-nav-drop");
const sideNavDropBtnsRotate = document.querySelectorAll(
  ".side-nav-drop-btn .fa-chevron-down"
);

sideNavDropBtns.forEach((sideNavDropBtn, idx) => {
  sideNavDropBtn.addEventListener("click", () => {
    sideNavDrops[idx].classList.toggle("active");
    sideNavDropBtnsRotate[idx].classList.toggle("rotate");
  });
});

// side-nav
const sideNavBtn = document.querySelector(".side-nav-btn");
const sideNavCloseBtn = document.querySelector(".side-nav-close-btn");
const sideNav = document.querySelector(".side-nav");

sideNavBtn.addEventListener("click", () => {
  sideNavBtn.classList.toggle("active");
  sideNav.classList.toggle("active");
});

sideNavCloseBtn.addEventListener("click", () => {
  sideNavBtn.classList.remove("active");
  sideNav.classList.remove("active");
});

// sticky-nav
let lastScrollTop = 0;

const header = document.querySelector("header");
const mobileHeader = document.querySelector(".mobile-header");

const stickyNav = (event) => {
  window.addEventListener("scroll", () => {
    let scrollTop = window.pageXOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
      event.style.top = "-200px";
    } else {
      event.style.top = "0";
    }
    lastScrollTop = scrollTop;
  });
};

stickyNav(header);
stickyNav(mobileHeader);

// button animation
const button = document.querySelectorAll("button");
if (button[0]) {
  button.forEach((btn) => {
    btn.addEventListener("mousedown", () => {
      btn.classList.add("animate");
    });

    btn.addEventListener("mouseup", () => {
      btn.classList.remove("animate");
    });

    btn.addEventListener("mouseout", () => {
      btn.classList.remove("animate");
    });
  });
}


