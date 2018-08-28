# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc
from textwrap import dedent

import reusable_components as reusable


def SectionTitle(title):
    return dcc.Markdown(dedent('''    
    ***

    ## {}
    '''.format(title)))


def AppSection(app_name,
               app_link,
               code_link,
               img_src,
               description,
               code_name_display_text='Source code',
               width=6):
    if code_link:
        links = dedent(
            '''
            [{}]({}) | [{}]({})
            '''.format(app_name, app_link, code_name_display_text, code_link)
        )
    else:
        links = dedent(
            '''
            [{}]({})
            '''.format(app_name, app_link)
        )

    return reusable.Column(
        width=width,
        children=[
            html.A(
                className='image-link',
                href=app_link,
                children=html.Img(
                    src=img_src,
                    alt='Screenshot of {}'.format(app_name)
                )
            ),
            dcc.Markdown(
                className="markdown-links",
                children=links
            ),
            dcc.Markdown(dedent(description))
        ]
    )


layout = html.Div(className='gallery', children=[

    # Getting Started Section
    dcc.Markdown(dedent('''

    # Dash Gallery

    ***

    ## Getting Started
    ''')),

    reusable.Row([
        html.A(
            className='image-link',
            href='https://dash.plot.ly/getting-started',
            children=html.Img(
                src='https://github.com/plotly/dash-docs/raw/master/images/gapminder-animation.gif',
                alt='Screenshot of simple Dash app'
            )
        ),

        dcc.Markdown(
            className="markdown-links",
            children=dedent('''
            [View the getting started guide](https://dash.plot.ly/getting-started)
            ''')
        ),

        dcc.Markdown(dedent('''
        
        The [Dash Getting Started Guide](/getting-started) contains
        many applications that range in complexity.
    
        The first interactive app that you'll create combines a `Slider`
        with a `Graph` and filters data using a Pandas `DataFrame`.
        The `animate` property in the `Graph` component was set to `True`
        so that the points transition smoothly.
        Some interactivity is built-in to the `Graph` component including
        hovering over values, clicking on legend items to toggle traces, and
        zooming into regions.
    
        ''')),
    ]),

    # FINANCE SECTION
    SectionTitle('Finance'),

    reusable.Row([
        AppSection(
            app_name='Stock Tickers',
            app_link='https://dash-stock-tickers.plot.ly',
            code_link='https://github.com/plotly/dash-stock-tickers-demo-app',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/stock-tickers.png',
            description='''
            This app queries data from Google Finance and displays the results as candlestick
            charts. Dash comes with several financial chart types including candlestick
            charts, OHLC graphs, time series, and range sliders.
        
            This app was written in just around 100 lines of code.
            '''
        ),

        AppSection(
            app_name='Vanguard Report',
            app_link='https://vanguard-report.herokuapp.com/',
            code_link='https://github.com/plotly/dash-vanguard-report',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/vanguard.gif',
            description='''
            This app recreates the look and feel of a Vanguard report.
            It includes a Print to PDF button and the styles were optimized
            to look good on the web and in PDF form.
        
            The charts in the report on the web version are interactive.
            You can hover over points to see their values and zoom into
            regions. Since this report was built on top of Dash, you could
            adapt this report to include even more interactive elements, like
            a dropdown or a search box.
        
            With PDF styles, you can hide and show elements depending on whether
            the app is being viewed in the web browser or in print, using the
            same framework for the rich interactive applications as the static
            PDF reports.
            '''

        )
    ]),

    reusable.Row([
        AppSection(
            app_name='3D Yield Curve',
            app_link='https://dash-yield-curve.plot.ly',
            code_link='https://github.com/plotly/dash-yield-curve',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-yield-curve-app.png',
            description='''
            This Dash app adapts the excellent NY Times
            report [A 3-D View of a Chart That Predicts The Economic Future: The Yield Curve](https://www.nytimes.com/interactive/2015/03/19/upshot/3d-yield-curve-economic-growth.html).

            Dash comes with a wide range of interactive 3D chart types,
            such as 3D scatter plots, surface plots, network graphs and ribbon plots.
            [View more 3D chart examples](https://plot.ly/python/3d-charts/).
            '''
        ),

        AppSection(
            app_name='Recession in 255 Charts',
            app_link='https://dash-recession-report.plot.ly',
            code_link='https://github.com/plotly/dash-recession-report-demo',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/nytimes.png',
            description='''
            485 lines of Python code, including text copy.
        
            This Dash app was adapted from NYTimes's excellent
            [How the Recession Reshaped the Economy in 255 Charts](https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html).
        
            This Dash app displays its content linearly, like an
            interactive report. The report highlights several notable
            views of the data and then invites the user to highlight
            their own regions at the end. This method of highlighting
            views is a great strategy for walking your readers through
            your complex analysis.
        
            The height of the charts was specified in viewport units (`vh`),
            scaling the size of the chart to the height of the screen. It
            looks great on monitors big and small.
        
            The text in the application is centered and its width is restricted
            to improve the reading experience. The graphs are full bleed:
            the extend past the narrow column of text the edges of page.
            '''
        )
    ]),

    # ENERGY AND TRANSPORT SECTION
    SectionTitle('Energy and Transportation'),

    reusable.Row([
        AppSection(
            app_name='Natural Gas Well Production',
            app_link='https://dash-oil-and-gas.plot.ly',
            code_link='https://github.com/plotly/dash-oil-and-gas-demo',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/oil-and-gas.gif',
            description='''
            This Dash app displays well data from New York State. As you hover over
            values in the map, a time series is displayed showing production values
            over time. As you change the years in the range slider, the aggregate
            time series is updated with the sum of all production over time.
            The histogram chart is also selectable, serving as an alternative
            control for selecting a range of time.
            
            This application is also mobile-friendly. Dash apps are built and
            published in the Web, so the full power of CSS is available.
            The Dash core team maintains a [core style guide here](https://codepen.io/chriddyp/pen/bWLwgP)
            that  includes a responsive 12 column grid.
            '''
        ),

        AppSection(
            app_name='NYC Uber Rides',
            app_link='https://dash-uber-rides.plot.ly',
            code_link='https://github.com/plotly/dash-uber-rides-demo',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/uber-rides.gif',
            description='''
            This app displays all of the Uber rides in New York City in 2014.
            The original datafile is almost 500MB large and all of the filtering is
            done in memory with Pandas. Buttons on the chart itself highlight
            different regions in the city.
            '''
        )
    ]),

    # LIFE SCIENCES SECTION
    SectionTitle('Life sciences'),

    reusable.Row([
        AppSection(
            app_name='Drug Precursors',
            app_link='https://dash-drug-explorer.plot.ly',
            code_link='https://github.com/plotly/dash-drug-discovery-demo/',
            img_src='https://github.com/plotly/dash-docs/raw/master/images/drug-discovery-app.gif',
            description='''
            This app displays a description of the drug as you hover over points in the
            graph.
        
            Selecting drugs in the dropdown highlights their position in the chart and
            appends their symbol in the table below.
        
            Built in a few hundred lines of Python code.
            '''

        ),

        AppSection(
            app_name='MRI Reconstruction',
            app_link='http://brain-surface-viewer.herokuapp.com/',
            code_link='https://github.com/plotly/dash-brain-surface-viewer',
            img_src='https://raw.githubusercontent.com/plotly/dash-brain-surface-viewer/master/ZOMBIE_BRAIN.png',
            description='''
            🐭 Explore human and mice brains in 3d.
            
            Add interactive labels to points on the brain surface and change the surface colorscale.
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='Phylogeny trees and global spread of 6 viruses',
            app_link='https://dash-phylogeny.herokuapp.com/',
            code_link='https://github.com/plotly/dash-phylogeny',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-phylo-tree.gif',
            description='''
            Interactively explore the propagation of 6 viruses, by time and/or by geolocalisation. 
            In the online app, you can select a virus, and the evolution of the virus as a phylogeny tree will display with a map and time series of the virus's global spread.
        ''',
            width=12
        )
    ]),

    # GOVERNMENT AND PUBLIC HEALTH
    SectionTitle('Government & Public Health'),

    reusable.Row([
        AppSection(
            app_name='US Opioid Epidemic',
            app_link='https://opioid-epidemic.herokuapp.com/',
            code_link='https://github.com/plotly/dash-opioid-epidemic-demo',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/opioid-epidemic.png',
            description='''
            Interactively explore the effect of the opioid epidemic in North America.
            ''',
            width=12
        )
    ]),

    # MACHINE LEARNING AND COMPUTER VISION
    SectionTitle('Machine Learning & Computer Vision'),

    reusable.Row([
        AppSection(
            app_name='Object Detection',
            app_link='https://dash-object-detection.plot.ly/',
            code_link='https://github.com/plotly/dash-object-detection',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-object-detection.gif',
            description='''
            This object-detection app provides useful visualizations about 
            what's happening inside a complex video in real-time. The data 
            is generated using 
            [MobileNet v1](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) 
            in Tensorflow, trained on the COCO dataset. The video is 
            displayed using the community-maintained 
            [video component](https://community.plot.ly/t/modifying-a-dom-property-in-html-video-dash-video-component/7649).
            '''
        ),

        AppSection(
            app_name='Visualize Model Training',
            app_link='https://dash-live-model-training.plot.ly/',
            code_link='https://github.com/plotly/dash-live-model-training',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-live-model-training.gif',
            description='''
            For every Deep Learning models, keeping track of accuracy 
            and loss is an essential part of the training process, 
            since they indicate how good your models are. This app is 
            a real-time visualization app that monitors core metrics 
            of your Tensorflow graphs during the training, so that you 
            can quickly detect anomalies within your model.
            '''
        ),
    ]),

    reusable.Row([
        AppSection(
            app_name='Image Processing',
            app_link='http://dash-image-processing.plot.ly/',
            code_link='https://github.com/plotly/dash-image-processing',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-image-processing.gif',
            description='''
            This app wraps Pillow, a powerful image processing library in 
            Python, and abstracts all the operations through an 
            easy-to-use GUI. All the computation is done on the back-end 
            through Dash, and image transfer is optimized through 
            session-based Redis caching and S3 storage.
            '''
        ),

        AppSection(
            app_name='Interactive t-SNE',
            app_link='https://dash-tsne.plot.ly/',
            code_link='https://github.com/plotly/dash-tsne',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-tsne.gif',
            description='''
            t-SNE is a visualization algorithm that projects your 
            high-dimensional data into a 2D or 3D space so that you can 
            explore the spatial distribution of your data. The t-SNE 
            Explorer lets you interactively explore iconic image datasets 
            such as MNIST, and state-of-the-art word embeddings such as 
            GloVe, with all the computation done ahead of time. Data 
            point previews and graphs help you better understand the 
            dataset.
            '''
        ),
    ]),

    reusable.Row([
        AppSection(
            app_name='Explore SVMs',
            app_link='https://dash-svm.plot.ly/',
            code_link='https://github.com/plotly/dash-svm',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-svm.gif',
            description='''
            This app lets you explore Support Vector Clustering (a type 
            of Support Vector Machine) with UI input parameters. Toy datasets 
            and useful ML metrics plots are included. It is fully written in 
            Dash + scikit-learn.
            ''',
            width=12
        )
    ]),

    # BIG DATA
    SectionTitle('Big Data'),

    reusable.Row([
        AppSection(
            app_name='Dash Datashader',
            app_link='https://dash-datashader.herokuapp.com',
            code_link='https://github.com/plotly/dash-datashader',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-datashader.png',
            description='''
            Visualize hundreds of millions of points interactively with Dash and Datashader.
            ''',
            width=12
        )
    ]),

    # LIVE UPDATES SECTION
    SectionTitle('Live Updates'),

    reusable.Row([
        AppSection(
            app_name='Window Speed Measurement',
            app_link='https://dash-live-wind-data.plot.ly',
            code_link='https://github.com/plotly/dash-wind-streaming',
            img_src='https://raw.githubusercontent.com/plotly/dash-wind-streaming/d84b15eebf2c502372740416d445e8e3f23d0619/Gif/dash-wind-streaming.gif',
            description='''
            This app continually queries a SQL database and displays live charts of
            wind speed and wind direction. In Dash, the [dcc.Interval](https://dash.plot.ly/live-upates)
            component can be used to update any element on a recurring interval.
            ''',
            width=12
        )
    ]),

    # COMPONENT LIBRARIES SECTION
    SectionTitle('Component Libraries'),

    reusable.Row([
        AppSection(
            app_name='Join the discussion',
            app_link='https://community.plot.ly/t/display-tables-in-dash/4707/38',
            code_link='https://github.com/plotly/dash-table-experiments',
            img_src='https://raw.githubusercontent.com/plotly/dash-table-experiments/master/images/DataTable.gif',
            description='''
        Dash is currently incubating an interactive table component that provides
        built-in filtering, row-selection, editing, and sorting.
        Prototypes of this component are being developed in the
        [`dash-table-experiments`](https://github.com/plotly/dash-table-experiments)
        repository. Join the discussion in the
        [Dash Community Forum](https://community.plot.ly/t/display-tables-in-dash/4707/38).

        This example was written in ~100 lines of code.
        '''
        ),
        AppSection(
            app_name='Dash Community Components',
            app_link='https://community.plot.ly/t/show-and-tell-community-thread/7554',
            code_link=None,
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-community-components.png',
            description='''
        Dash has a [plugin system](https://dash.plot.ly/plugins) for integrating your own React.js components. 
        The Dash community has built many of their component libraries, like 
        [Video Components](https://community.plot.ly/t/modifying-a-dom-property-in-html-video/7649/11) 
        and [Large File Upload](https://community.plot.ly/t/show-and-tell-dash-resumable-upload/9519). 
        View more community maintained components and other projects in the Dash Community Forum’s 
        [Show and Tell Thread](https://community.plot.ly/t/show-and-tell-community-thread/7554)
        '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='Dash Core Components',
            app_link='https://dash.plot.ly/dash-core-components',
            code_link='https://github.com/plotly/dash-core-components',
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-core-components.png',
            description='''
        Dash comes with a set of rich components like sliders, dropdowns, graphs, and more. 
        [View the official Dash documentation to learn more](https://dash.plot.ly/dash-core-components).
        ''',
            width=12
        )

    ]),

    # DASH DAQ SECTION
    SectionTitle('Data Acquisition (DAQ)'),

    reusable.Row(
        dcc.Markdown(dedent(
            """
            Dash DAQ is a Dash component library for building custom data 
            acquisition interfaces with Dash in Python. Dash DAQ is a commercially licensed 
            product. [Learn more about Dash DAQ](https://www.dashdaq.io/).
            """
        ))
    ),

    reusable.Row([
        AppSection(
            app_name='Omega CN32PT-440-DC PID Controller',
            app_link='https://www.dashdaq.io/operate-an-omega-cn32pt-440-dc-pid-controller-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-omega-pid.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/07/Dash-DAQ-Omega-Platnium-Controller-146@05x.jpg',
            description='''
            Let’s heat things up with Dash DAQ! With this application, we use 
            Python to monitor and manage a PID controller connected to a water 
            heater 🔥
            '''
        ),

        AppSection(
            app_name='Wireless Arduino Robot',
            app_link='https://www.dashdaq.io/control-a-wireless-arduino-robot-in-python',
            code_name_display_text='Try the app',
            code_link='http://dash-daq-sparki.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/07/Dash-DAQ-Sparki-11-Edit@05x.jpg',
            description='''
            We love our robots here at Plotly! This Dash DAQ app wirelessly 
            controls Sparki, an Arduino-based robot 🤖
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='I-V curve tracer with a Keithley 2400 SourceMeter',
            app_link='https://www.dashdaq.io/build-an-i-v-curve-tracer-with-a-keithley-2400-sourcemeter-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-iv-tracer.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/07/IMG_0345@05x.jpg',
            description='''
            With this Dash DAQ application written in Python, you can create 
            UI components to interface with a Keithley 2400 SourceMeter.
            '''
        ),

        AppSection(
            app_name='Control a Robotic Arm',
            app_link='https://www.dashdaq.io/control-a-robotic-arm-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-robotic-arm-edge.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/07/Dash-DAQ-Robotic-Arm-Edge-19@05x.jpg',
            description='''
            Dash DAQ’s GUI components let you interface with all the robot’s 
            motors and LED, even from a mobile device… just as if it were a 
            real remote control! 🤖
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='Ocean Optics Spectrometer',
            app_link='https://www.dashdaq.io/control-an-ocean-optics-spectrometer-in-python',
            code_name_display_text='Try the app',
            code_link='http://dash-ocean-optics.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/06/Dash-DAQ-_-Ocean-Optics-2@05x.jpg',
            description='''
            We wrote a Dash DAQ application in Python to 
            control and read an Ocean Optics spectrometer with interactive UI 
            components.
            '''
        ),
        AppSection(
            app_name='Kurt J. Lesker Pressure Gauge Controller',
            app_link='https://www.dashdaq.io/read-pressure-from-kurt-j-lesker-gauge-controller-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-pressure-gauge-kjl.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/06/Dash-DAQ-Kurt@05x.jpg',
            description='''
            A Dash DAQ application, written in Python, gives you clean, modern 
            UI components to facilitate the readout of a Kurt J. Lesker 
            pressure gauge controller.
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='Read Accelerometer Data',
            app_link='https://www.dashdaq.io/read-phidgets-accelerometer-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-accelerometer.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/06/Dash-DAQ-_-Accelerometer@05x.jpg',
            description='''
            Running tests with an accelerometer? Dash DAQ gives you the 
            components you need to write rich, flexible GUIs for interfacing 
            with your instruments in Python.
            '''
        ),
        AppSection(
            app_name='Control an LED Strip',
            app_link='https://www.dashdaq.io/control-an-led-strip-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-led.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/05/Dash-DAQ-_-Blank-Stick-main@05x.jpg',
            description='''
            Team Plotly is getting colorful with Dash DAQ! This application 
            controls the colored LED lights in a BlinkStick. We even wrote a 
            Rainbow mode🌈
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='Control a Stepper Motor',
            app_link='https://www.dashdaq.io/stepper-motor-control-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-stepper-motor.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/04/Dash-DAQ-_-Stepper-Motor@05x.jpg',
            description='''
            From 3D printers, to mirror mounts, to machine tools – stepper 
            motors are ubiquitous. Using Dash DAQ, we created a GUI to control 
            a Silverpak 17C Lin Engineering stepper motor.
            '''
        ),
        AppSection(
            app_name='Tektronix Oscilloscope Data Logging',
            app_link='https://www.dashdaq.io/oscilloscope-logging-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-tektronix-350.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/04/Dash-DAQ-_-Tektronix-Oscilloscope-Tektronic-Function-Generator@05x-1.jpg',
            description='''
            Whether testing your power supply or monitoring a heartbeat, if 
            you have an oscilloscope, Dash DAQ will help you control and read 
            your instrument with user-friendly GUIs.
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='B&K Precision Power Supply',
            app_link='https://www.dashdaq.io/control-bk-precision-1785b-power-supply-in-python',
            code_name_display_text='Try the app',
            code_link='http://dash-daq-bkprecision.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/03/Dash-DAQ-_-BKprecision@05x-1.jpg',
            description='''
            This Dash DAQ app controls a B&K Precision power supply using a 
            clean and functional UI, written in just over 300 lines of Python 
            code.
            '''
        ),
        AppSection(
            app_name='Agilent 34401A Multimeter',
            app_link='https://www.dashdaq.io/read-agilent-34401a-multimeter-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-hp-multimeter.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/03/Dash-DAQ-_-Multimeter-zoom@05x.jpg',
            description='''
            Here’s how we used Dash DAQ’s interactive UI components to 
            control the HP Agilent 34401A Multimeter.
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='Tektronix Function Generator',
            app_link='https://www.dashdaq.io/control-tektronix-function-generator-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-tektronix-350.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/03/Dash-DAQ-_-Tektronix-Oscilloscope-Tektronic-Function-Generator-zoom@05x.jpg',
            description='''
            A function generator generates a variety of electrical waveforms. 
            This Dash DAQ application facilitates the control of a Tektronix 
            AFG3021 function generator.
            '''
        ),
        AppSection(
            app_name='Pfeiffer Vacuum Gauge',
            app_link='https://www.dashdaq.io/read-pfeiffer-vacuum-gauge-pressure-in-python',
            code_name_display_text='Try the app',
            code_link='https://dash-daq-pressure-gauge-pv.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/03/Dash-DAQ-_-Pfeiffer@05x.jpg',
            description='''
            In just over 300 lines of code, this app helps you control 
            and read a Pfeiffer vacuum gauge controller.
            '''
        )
    ]),

    reusable.Row([
        AppSection(
            app_name='Analyze Frequency Responses using a Tektronix Function Generator and Oscilloscope',
            app_link='https://www.dashdaq.io/analyze-frequency-responses-in-python-using-a-tektronix-function-generator-and-oscilloscope',
            code_name_display_text='Try the app',
            code_link='https://freq-response-plotter.herokuapp.com/',
            img_src='https://www.dashdaq.io/wp-content/uploads/2018/07/Dash-DAQ-_-Tektronix-Oscilloscope-Tektronic-Function-Generator.jpg',
            description='''
            With this Dash DAQ app, you can create a user-friendly GUI for 
            analyzing the frequency responses of circuits.
            ''',
            width=12
        )
    ]),

    # DASH DOC SECTION
    SectionTitle('Dash Documentation'),

    reusable.Row([
        dcc.Markdown(dedent('''
        These Dash docs that you're looking at? They are itself a Dash app!
        ''')),

        AppSection(
            app_name='View Dash User Guide Source Code',
            app_link='https://github.com/plotly/dash-docs',
            code_link=None,
            img_src='https://raw.githubusercontent.com/plotly/dash-docs/master/images/dash-home-page.png',
            description='',
            width=12
        )
    ]),
])
