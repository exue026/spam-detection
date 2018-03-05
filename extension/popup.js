function setup() {
  const text = document.getElementById('raw-text').value

  chrome.storage.local.set({
    classifyText: text,
  }, function() {
    chrome.tabs.executeScript({
      file: 'classify.js'
    })
  })
}

const classifyButton = document.getElementById('goclassify')
classifyButton.addEventListener('click', setup)
