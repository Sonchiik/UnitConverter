document.addEventListener("DOMContentLoaded", function(){
    showForm('Length');
});

async function showForm(formId) {
    const forms = document.querySelectorAll('.converterForm');
    forms.forEach(form => form.style.display = 'none');
    document.getElementById(`${formId}Form`).style.display = 'block';
}

async function convertUnit(type) {
    const value = document.getElementById(`value_${type}`).value;
    const fromUnit = document.getElementById(`from_unit_${type}`).value;
    const toUnit = document.getElementById(`to_unit_${type}`).value;

    const requestData = {
        value: parseFloat(value),
        from_unit: fromUnit,
        to_unit: toUnit
    };

    const base_URL = "http://127.0.0.1:8000";
    const endpoint = `/convert/${type}`;

    try {
        const response = await fetch(base_URL + endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        console.log("Response data:", data);

        const resultField = document.getElementById(`result_${type}`);
        resultField.style.display = 'block';
        resultField.textContent = `${value} ${fromUnit} = ${data.result.toFixed(2)} ${toUnit}`;

    } catch (error) {
        console.error("Error:", error);
    }
}
