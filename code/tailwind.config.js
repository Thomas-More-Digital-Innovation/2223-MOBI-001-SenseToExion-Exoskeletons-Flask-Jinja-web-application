/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./static/src/**/*.js"
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require("daisyui")
    ],
    daisyui: {
        themes: [
            {
                thomas_more: {
                    "primary": "#009CAB",
                    "secondary": "#F04C25",
                    "accent": "#575757",
                    "neutral": "#373737",
                    "base-100": "#FFFFFF",
                    "info": "#3ABFF8",
                    "success": "#36D399",
                    "warning": "#FBBD23",
                    "error": "#F87272",
                }
            }
        ]
    }
}
