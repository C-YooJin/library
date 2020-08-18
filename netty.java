public class netty {
    public void start() {
        KafkaManager.getInstance();

        // netty channel 관련 생성자 생성 (부모, 자식)
        EventLoopGroup parentGroup = new NioEventLoopGroup(1);	// 생성자 1이므로 단일 스레드로 동작하는 객체다
        EventLoopGroup childGroup = new NioEventLoopGroup();	// 생성자에 인수가 없으므로 cpu 코어 수에 따라 설정 된다

        // netty bootstrap 생성자 생성
        ServerBootstrap serverBootstrap = new ServerBootstrap();

        // 위에서 생성한 부모, 자식 채널에 대해.. bootstrap 그룹핑 및 이런 저런 설정들
        serverBootstrap.group(parentGroup,childGroup)
                .channel(NioServerSocketChannel.class) // 부모쓰레드 입출력모두 설정, NIO모드
                .localAddress( new InetSocketAddress(host,port))
                .option(ChannelOption.SO_BACKLOG,100)
                .handler(new LoggingHandler(LogLevel.INFO))
                .childHandler(new ChannelInitializer<SocketChannel>() { // 자식 채널 초기화
                    @Override
                    protected void initChannel(SocketChannel socketChannel) throws Exception {
                        socketChannel.pipeline().addLast(
                                new SimpleServeHandler()
                        );
                    }
                } );
        try {
            g1 = parentGroup;
            g2 = childGroup;

            logger.info("server starting... host:{},port:{}", host,port);
            ChannelFuture channelFuture = serverBootstrap.bind().sync();  // start th server

            // 서버 종료할 때 프로세스
            channelFuture.channel().closeFuture().sync();  // wait until the server socket is closed
            logger.info("after closeFuture sync");
        } catch (InterruptedException e) {
            logger.info("occur InterruptedException");
            e.printStackTrace();

        } finally {

            g1 = null;
            g2 = null;

            // 셧다운
            childGroup.shutdownGracefully();
            parentGroup.shutdownGracefully();

            logger.info("childGroup, parentGroup shutdownGraceFully()");
        }

        HordeDataSource.shutdown();
        logger.info("종료됨");
    }
}
}
