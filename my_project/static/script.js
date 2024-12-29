document.addEventListener("DOMContentLoaded", function() {
                                    // Get the button and h1 elements
                                    const button = document.getElementById("changeTextButton");
                                    const welcomeMessage = document.querySelector("h1");

                                    // Event listener for button click
                                    button.addEventListener("click", function() {
                                        // Change the text content of the h1 element when button is clicked
                                        welcomeMessage.textContent = "You clicked the button! The text has changed.";
                                    });
                                });
                