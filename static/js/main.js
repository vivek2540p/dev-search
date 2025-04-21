

let searchForm = document.getElementById('fsearch')
let pageLinks = document.getElementsByClassName('page-link')

if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()
            let page = this.dataset.page
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            searchForm.submit()
        })
    }
}



let tags = document.getElementsByClassName('project-tag')

for (let i = 0; tags.length > i; i++) {
    tags[i].addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project



        fetch('http://127.0.0.1:8000/api/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'project': projectId, 'tag': tagId })
        })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })

    })
}



function toggleChat() {
    const chat = document.getElementById("chatContainer");
    chat.style.display = chat.style.display === "flex" ? "none" : "flex";
  }

  function sendMessage() {
    const input = document.getElementById("userInput");
    const messages = document.getElementById("chatMessages");
  
    if (input.value.trim() !== "") {
      const userText = input.value;
      const projectId = document.getElementById("projectId").value;
      const userMsg = document.createElement("p");
      userMsg.className = "human-message";
      userMsg.innerHTML = userText;
      messages.appendChild(userMsg);

      const loadingMsg = document.createElement("p");
    loadingMsg.className = "loading-message";
    loadingMsg.innerHTML = "Loading...";
    messages.appendChild(loadingMsg);
  
      fetch("http://127.0.0.1:8000/projects/chatbot/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        //   "X-CSRFToken": getCookie("csrftoken")  // Handle CSRF for Django
        },
        body: JSON.stringify({ message: userText, project: projectId })
      })
      .then(response => response.json())
      .then(data => {
        messages.removeChild(loadingMsg);
        const botMsg = document.createElement("p");
        botMsg.className = "bot-message";
        botMsg.innerHTML = data.response;
        messages.appendChild(botMsg);
        messages.scrollTop = messages.scrollHeight;
      }).catch(error => {
        // Handle any errors during the fetch
        messages.removeChild(loadingMsg);
        const errorMsg = document.createElement("p");
        errorMsg.className = "error-message";
        errorMsg.innerHTML = "Something went wrong, please try again!";
        messages.appendChild(errorMsg);
        sendButton.disabled = false;
      });
  
  
      input.value = "";
    }
  }
  
