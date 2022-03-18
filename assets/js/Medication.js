function myFunction() {
  // Get the checkbox
  var checkBox = document.getElementById("medicationCheck");
  // Get the output text
  var text = document.getElementById("MedicationErrorDiv");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    div.style.display = "block";
  } else {
    div.style.display = "none";
  }
}