function translateText() {
  const text = document.getElementById("inputText").value;
  const target_language = document.getElementById("targetLanguage").value;
  const source_language = document.getElementById("sourceLanguage").value;

  fetch('/translate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ text, target_language, source_language })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("outputText").innerText = data.translated_text;
    document.getElementById("detectedLang").innerText = `Source language: ${data.detected_language}`;
  });
}

function startVoice() {
  const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
  recognition.lang = 'en-US';
  recognition.start();
  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById("inputText").value = transcript;
  };
}

function speakText() {
  const output = document.getElementById("outputText").innerText;
  const speech = new SpeechSynthesisUtterance(output);
  speech.lang = 'auto';
  window.speechSynthesis.speak(speech);
}
