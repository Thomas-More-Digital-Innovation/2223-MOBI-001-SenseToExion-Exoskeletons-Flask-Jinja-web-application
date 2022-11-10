/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./static/src/**/*.js"
    ],
    theme: {
        extend: {
            backgroundImage:{
                'DOF-1': "url('../static/images/exoskeleton.png"
            }
        },
    },
    plugins: [
        require("daisyui")
    ]
}

