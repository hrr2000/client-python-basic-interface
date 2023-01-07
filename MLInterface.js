async function runModel(modelName, parameters) {
    return fetch('http://localhost:8080', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            model_name: modelName,
            parameters
        })
    })
}