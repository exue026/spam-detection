chrome.storage.local.get('classifyText', function (items) {
    console.log(items)
    handleText(items.classifyText)
    chrome.storage.local.remove('classifyText')
})

function handleText(text) {
    formattedText = text.trim().replace(/\s\s+/g, ' ')
    if (formattedText.split(' ').length < 50) {
        alert(`
            ERROR: Text must be at least 50 words in length in
            order for it to be classifed with an acceptable degree
            of accuracy. Please try again with a larger piece
            of text.
        `)
        return
    }
    // send http request to python web server
}