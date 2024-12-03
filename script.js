async function runDfaf() {
    const input = document.getElementById('dfaf-input').value.split(',').map(Number);
    const a = parseFloat(document.getElementById('dfaf-a').value);
    const iterations = parseInt(document.getElementById('dfaf-iterations').value);

    const response = await fetch('/api/dfaf', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ x: input, a: a, n_iterations: iterations })
    });

    const data = await response.json();
    alert(`D-FAF Result: ${data.result}`);
}

async function runPfaf() {
    const input = document.getElementById('pfaf-input').value.split(',').map(Number);
    const a = parseFloat(document.getElementById('pfaf-a').value);
    const iterations = parseInt(document.getElementById('pfaf-iterations').value);
    const noiseLevel = parseFloat(document.getElementById('pfaf-noise').value);

    const response = await fetch('/api/pfaf', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ x: input, a: a, n_iterations: iterations, noise_level: noiseLevel })
    });

    const data = await response.json();
    alert(`P-FAF Result: ${data.result}`);
}
