// app.js
// Frontend logic for AI Resume Matcher

const matchButton = document.getElementById("matchBtn");
const resultBox = document.getElementById("result");

matchButton.addEventListener("click", async () => {
  const resumeText = document.getElementById("resume").value.trim();
  const jobText = document.getElementById("job").value.trim();

  if (!resumeText || !jobText) {
    resultBox.innerText = "Please paste both resume and job description.";
    return;
  }

  resultBox.innerText = "Analyzing with AI... 🤖";

  try {
    // 🔧 MOCK MODE (until backend is live)
    const mockScore = Math.floor(Math.random() * 30) + 65;

    setTimeout(() => {
      resultBox.innerText = `Match Score: ${mockScore}%`;
    }, 1200);

    // REAL BACKEND (enable later)
    /*
    const response = await fetch("http://localhost:8000/match", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        resume_text: resumeText,
        job_text: jobText,
      }),
    });

    const data = await response.json();
    resultBox.innerText = `Match Score: ${data.match_score}%`;
    */

  } catch (error) {
    resultBox.innerText = "Something went wrong. Try again.";
    console.error(error);
  }
});
