let formInputLabels = document.querySelectorAll(".form-input-label");
const goBackBtn = document.querySelector(".back-btn");

function getData(data) {
  formInputLabels.forEach((formInputLabel) => {
    let dataAttributeName = data.getAttribute("name");
    let labelAttributeName = formInputLabel.getAttribute("name");

    if (dataAttributeName === labelAttributeName) {
      if (data.getAttribute("name") === dataAttributeName) {
        data.value.length
          ? formInputLabel.classList.add("shrink")
          : formInputLabel.classList.remove("shrink");
      }
    }
  });
}

goBackBtn.addEventListener("click", () => {
  history.back();
});
