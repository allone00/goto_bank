'use strict';

const path = require('path');
const webpack = require('webpack');


module.exports = {
    mode: 'development',

    entry: './js/app.js',

    optimization: {
        minimize: false
    },


    output: {
        path: path.resolve(__dirname, 'static/dist'),
        filename: 'bundle.js',
        publicPath: '/dist'
    },

    module: {
        rules: [
            {
                test: /\.js$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        'presets': ['env', 'es2015', 'stage-0', 'stage-1', 'stage-2', 'react'],
                        'plugins': ['transform-es2015-destructuring', 'transform-object-rest-spread']
                    }
                }
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },

        ]
    }
};